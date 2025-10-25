from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from huggingface_hub import login
import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

# 🔑 Hugging Face login
login(token=HF_TOKEN)

# 📦 Load model
MODEL_ID = "mrm8488/bert-tiny-finetuned-fake-news-detection"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, token=HF_TOKEN)
fake_news_detector = pipeline("text-classification", model=model, tokenizer=tokenizer)

app = Flask(__name__)

# 🔍 Google FactCheck helper
def fact_check(text):
    API_KEY = os.getenv("FACTCHECK_API_KEY")

    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {"query": text, "key": API_KEY}
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code != 200:
            return {"verified": "unknown", "source": None, "full": data}

        if "claims" in data and len(data["claims"]) > 0:
            claim = data["claims"][0]
            verdict = claim.get("claimReview", [{}])[0].get("textualRating", "unknown")
            source = claim.get("claimReview", [{}])[0].get("publisher", {}).get("name")
            return {"verified": verdict, "source": source, "full": data}
        
        return {"verified": "unknown", "source": None, "full": data}
    
    except Exception as e:
        return {"verified": "error", "source": str(e), "full": None}

# 📝 Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if "text" not in data:
        return jsonify({"error": "Please provide 'text' in JSON body"}), 400

    text = data["text"]

    # 1️⃣ BERT prediction
    result = fake_news_detector(text)[0]
    label = "FAKE" if result["label"] == "LABEL_1" else "REAL"
    confidence = result["score"]

    # 2️⃣ FactCheck API
    fact_result = fact_check(text)

    # ✅ Combined output
    return jsonify({
        "text": text,
        "bert_label": label,
        "bert_score": confidence,
        "bert_prediction": label,
        "bert_confidence": confidence,
        "fact_verdict": fact_result["verified"],
        "fact_source": fact_result["source"],
        "fact_full_data": fact_result["full"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
