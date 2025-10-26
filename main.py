# # # # from flask import Flask, request, jsonify
# # # # from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
# # # # from huggingface_hub import login
# # # # import requests
# # # # import os

# # # # HF_TOKEN = os.getenv("HF_TOKEN")

# # # # # 🔑 Hugging Face login
# # # # login(token=HF_TOKEN)

# # # # # 📦 Load model
# # # # MODEL_ID = "mrm8488/bert-tiny-finetuned-fake-news-detection"
# # # # tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
# # # # model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, token=HF_TOKEN)
# # # # fake_news_detector = pipeline("text-classification", model=model, tokenizer=tokenizer)

# # # # app = Flask(__name__)

# # # # # 🔍 Google FactCheck helper
# # # # def fact_check(text):
# # # #     API_KEY = os.getenv("FACTCHECK_API_KEY")

# # # #     url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
# # # #     params = {"query": text, "key": API_KEY}
    
# # # #     try:
# # # #         response = requests.get(url, params=params)
# # # #         data = response.json()
# # # #         if response.status_code != 200:
# # # #             return {"verified": "unknown", "source": None, "full": data}

# # # #         if "claims" in data and len(data["claims"]) > 0:
# # # #             claim = data["claims"][0]
# # # #             verdict = claim.get("claimReview", [{}])[0].get("textualRating", "unknown")
# # # #             source = claim.get("claimReview", [{}])[0].get("publisher", {}).get("name")
# # # #             return {"verified": verdict, "source": source, "full": data}
        
# # # #         return {"verified": "unknown", "source": None, "full": data}
    
# # # #     except Exception as e:
# # # #         return {"verified": "error", "source": str(e), "full": None}

# # # # # 📝 Prediction endpoint
# # # # @app.route("/predict", methods=["POST"])
# # # # def predict():
# # # #     data = request.json
# # # #     if "text" not in data:
# # # #         return jsonify({"error": "Please provide 'text' in JSON body"}), 400

# # # #     text = data["text"]

# # # #     # 1️⃣ BERT prediction
# # # #     result = fake_news_detector(text)[0]
# # # #     label = "FAKE" if result["label"] == "LABEL_1" else "REAL"
# # # #     confidence = result["score"]

# # # #     # 2️⃣ FactCheck API
# # # #     fact_result = fact_check(text)

# # # #     # ✅ Combined output
# # # #     return jsonify({
# # # #         "text": text,
# # # #         "bert_label": label,
# # # #         "bert_score": confidence,
# # # #         "bert_prediction": label,
# # # #         "bert_confidence": confidence,
# # # #         "fact_verdict": fact_result["verified"],
# # # #         "fact_source": fact_result["source"],
# # # #         "fact_full_data": fact_result["full"]
# # # #     })

# # # # if __name__ == "__main__":
# # # #     app.run(host="0.0.0.0", port=5000)
# # # from flask import Flask, request, jsonify
# # # from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
# # # from huggingface_hub import login
# # # import requests
# # # import os
# # # import wikipedia
# # # from dotenv import load_dotenv
# # # # ===============================================
# # # # 🔐 Setup: Tokens and Hugging Face Login
# # # # ===============================================
# # # HF_TOKEN = os.getenv("HF_TOKEN")
# # # login(token=HF_TOKEN)

# # # MODEL_ID = "mrm8488/bert-tiny-finetuned-fake-news-detection"
# # # tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
# # # model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, token=HF_TOKEN)
# # # fake_news_detector = pipeline("text-classification", model=model, tokenizer=tokenizer)

# # # app = Flask(__name__)

# # # # ===============================================
# # # # 🔍 Helper 1: Google FactCheck API
# # # # ===============================================
# # # def fact_check(text):
# # #     API_KEY = os.getenv("FACTCHECK_API_KEY")
# # #     url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
# # #     params = {"query": text, "key": API_KEY}
    
# # #     try:
# # #         response = requests.get(url, params=params)
# # #         data = response.json()

# # #         if response.status_code != 200:
# # #             return {"verified": "unknown", "source": None, "full": data}

# # #         if "claims" in data and len(data["claims"]) > 0:
# # #             claim = data["claims"][0]
# # #             verdict = claim.get("claimReview", [{}])[0].get("textualRating", "unknown")
# # #             source = claim.get("claimReview", [{}])[0].get("publisher", {}).get("name")
# # #             return {"verified": verdict, "source": source, "full": data}

# # #         return {"verified": "unknown", "source": None, "full": data}

# # #     except Exception as e:
# # #         return {"verified": "error", "source": str(e), "full": None}

# # # # ===============================================
# # # # 📚 Helper 2: Quick Wikipedia Knowledge Base Check
# # # # ===============================================
# # # def wikipedia_check(text):
# # #     """
# # #     Tries to find a matching Wikipedia article for a claim.
# # #     Returns summary and confidence if relevant.
# # #     """
# # #     try:
# # #         search_results = wikipedia.search(text)
# # #         if not search_results:
# # #             return {"wiki_found": False, "wiki_summary": None, "wiki_source": None}

# # #         page_title = search_results[0]
# # #         page = wikipedia.page(page_title)
# # #         summary = page.summary[:600]  # limit length
# # #         url = page.url

# # #         return {
# # #             "wiki_found": True,
# # #             "wiki_summary": summary,
# # #             "wiki_source": url
# # #         }
# # #     except Exception as e:
# # #         return {"wiki_found": False, "wiki_summary": str(e), "wiki_source": None}

# # # # ===============================================
# # # # 🧾 Prediction Endpoint
# # # # ===============================================
# # # @app.route("/predict", methods=["POST"])
# # # def predict():
# # #     data = request.json
# # #     if "text" not in data:
# # #         return jsonify({"error": "Please provide 'text' in JSON body"}), 400

# # #     text = data["text"]

# # #     # 1️⃣ BERT fake-news prediction
# # #     result = fake_news_detector(text)[0]
# # #     label = "FAKE" if result["label"] == "LABEL_1" else "REAL"
# # #     confidence = round(result["score"], 3)

# # #     # 2️⃣ FactCheck API
# # #     fact_result = fact_check(text)

# # #     # 3️⃣ Wikipedia Fallback
# # #     wiki_result = wikipedia_check(text)

# # #     # ✅ Final combined response
# # #     return jsonify({
# # #         "input_text": text,
# # #         "bert_label": label,
# # #         "bert_confidence": confidence,
# # #         "fact_verdict": fact_result["verified"],
# # #         "fact_source": fact_result["source"],
# # #         "fact_full_data": fact_result["full"],
# # #         "wiki_found": wiki_result["wiki_found"],
# # #         "wiki_summary": wiki_result["wiki_summary"],
# # #         "wiki_source": wiki_result["wiki_source"]
# # #     })

# # # # ===============================================
# # # # 🚀 Run the server
# # # # ===============================================
# # # if __name__ == "__main__":
# # #     app.run(host="0.0.0.0", port=5000)
# # from flask import Flask, request, jsonify
# # from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
# # from huggingface_hub import login
# # import requests
# # import os
# # import wikipedia
# # from dotenv import load_dotenv

# # # ===============================================
# # # 🔐 Load environment variables from .env file
# # # ===============================================
# # load_dotenv()  # ✅ This was missing

# # HF_TOKEN = os.getenv("HF_TOKEN")
# # FACTCHECK_API_KEY = os.getenv("FACTCHECK_API_KEY")

# # if not HF_TOKEN:
# #     raise ValueError("❌ HF_TOKEN not found. Make sure it's set in your .env file.")

# # # Login to Hugging Face Hub
# # login(token=HF_TOKEN)

# # # ===============================================
# # # 🧠 Load BERT Fake News Detection Model
# # # ===============================================
# # MODEL_ID = "mrm8488/bert-tiny-finetuned-fake-news-detection"
# # tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
# # model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, token=HF_TOKEN)
# # fake_news_detector = pipeline("text-classification", model=model, tokenizer=tokenizer)

# # app = Flask(__name__)

# # # ===============================================
# # # 🔍 Helper 1: Google FactCheck API
# # # ===============================================
# # def fact_check(text):
# #     url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
# #     params = {"query": text, "key": FACTCHECK_API_KEY}
    
# #     try:
# #         response = requests.get(url, params=params)
# #         data = response.json()

# #         if response.status_code != 200:
# #             return {"verified": "unknown", "source": None, "full": data}

# #         if "claims" in data and len(data["claims"]) > 0:
# #             claim = data["claims"][0]
# #             verdict = claim.get("claimReview", [{}])[0].get("textualRating", "unknown")
# #             source = claim.get("claimReview", [{}])[0].get("publisher", {}).get("name")
# #             return {"verified": verdict, "source": source, "full": data}

# #         return {"verified": "unknown", "source": None, "full": data}

# #     except Exception as e:
# #         return {"verified": "error", "source": str(e), "full": None}

# # # ===============================================
# # # 📚 Helper 2: Wikipedia Knowledge Base Check
# # # ===============================================
# # def wikipedia_check(text):
# #     try:
# #         search_results = wikipedia.search(text)
# #         if not search_results:
# #             return {"wiki_found": False, "wiki_summary": None, "wiki_source": None}

# #         page_title = search_results[0]
# #         page = wikipedia.page(page_title)
# #         summary = page.summary[:600]
# #         url = page.url

# #         return {
# #             "wiki_found": True,
# #             "wiki_summary": summary,
# #             "wiki_source": url
# #         }
# #     except Exception as e:
# #         return {"wiki_found": False, "wiki_summary": str(e), "wiki_source": None}

# # # ===============================================
# # # 🧾 Prediction Endpoint
# # # ===============================================
# # @app.route("/predict", methods=["POST"])
# # def predict():
# #     data = request.json
# #     if "text" not in data:
# #         return jsonify({"error": "Please provide 'text' in JSON body"}), 400

# #     text = data["text"]

# #     # 1️⃣ BERT fake-news prediction
# #     result = fake_news_detector(text)[0]
# #     label = "FAKE" if result["label"] == "LABEL_1" else "REAL"
# #     confidence = round(result["score"], 3)

# #     # 2️⃣ FactCheck API
# #     fact_result = fact_check(text)

# #     # 3️⃣ Wikipedia fallback
# #     wiki_result = wikipedia_check(text)

# #     return jsonify({
# #         "input_text": text,
# #         "bert_label": label,
# #         "bert_confidence": confidence,
# #         "fact_verdict": fact_result["verified"],
# #         "fact_source": fact_result["source"],
# #         "wiki_found": wiki_result["wiki_found"],
# #         "wiki_summary": wiki_result["wiki_summary"],
# #         "wiki_source": wiki_result["wiki_source"]
# #     })

# # # ===============================================
# # # 🚀 Run the Server
# # # ===============================================
# # if __name__ == "__main__":
# #     app.run(host="0.0.0.0", port=5000)
# from flask import Flask, request, jsonify
# from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
# from huggingface_hub import login
# import requests
# import os
# import wikipedia
# from dotenv import load_dotenv

# # ===============================================
# # 🔐 Load environment variables from .env file
# # ===============================================
# load_dotenv()  # ✅ Ensures .env variables are loaded

# HF_TOKEN = os.getenv("HF_TOKEN")
# FACTCHECK_API_KEY = os.getenv("FACTCHECK_API_KEY")

# if not HF_TOKEN:
#     raise ValueError("❌ HF_TOKEN not found. Make sure it's set in your .env file.")

# # Login to Hugging Face Hub
# login(token=HF_TOKEN)

# # ===============================================
# # 🧠 Load BERT Fake News Detection Model
# # ===============================================
# MODEL_ID = "mrm8488/bert-tiny-finetuned-fake-news-detection"
# tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
# model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, token=HF_TOKEN)
# fake_news_detector = pipeline("text-classification", model=model, tokenizer=tokenizer)

# # 🌐 Initialize Flask app
# app = Flask(__name__)

# # ===============================================
# # 🔍 Helper 1: Google FactCheck API
# # ===============================================
# def fact_check(text):
#     """
#     Queries Google's Fact Check Tools API for claims related to the given text.
#     Returns verdict, source, and full JSON for detailed results.
#     """
#     url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
#     params = {"query": text, "key": FACTCHECK_API_KEY}
    
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()

#         if response.status_code != 200:
#             return {"verified": "unknown", "source": None, "full": data}

#         if "claims" in data and len(data["claims"]) > 0:
#             claim = data["claims"][0]
#             verdict = claim.get("claimReview", [{}])[0].get("textualRating", "unknown")
#             source = claim.get("claimReview", [{}])[0].get("publisher", {}).get("name")
#             return {"verified": verdict, "source": source, "full": data}

#         return {"verified": "unknown", "source": None, "full": data}

#     except Exception as e:
#         return {"verified": "error", "source": str(e), "full": None}

# # ===============================================
# # 📚 Helper 2: Wikipedia Knowledge Base Check
# # ===============================================
# def wikipedia_check(text):
#     """
#     Uses Wikipedia as a fallback to verify factual information when FactCheck has no data.
#     """
#     try:
#         search_results = wikipedia.search(text)
#         if not search_results:
#             return {"wiki_found": False, "wiki_summary": None, "wiki_source": None}

#         page_title = search_results[0]
#         page = wikipedia.page(page_title)
#         summary = page.summary[:600]
#         url = page.url

#         return {
#             "wiki_found": True,
#             "wiki_summary": summary,
#             "wiki_source": url
#         }
#     except Exception as e:
#         return {"wiki_found": False, "wiki_summary": str(e), "wiki_source": None}

# # ===============================================
# # 🧾 Prediction Endpoint
# # ===============================================
# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.json
#     if "text" not in data:
#         return jsonify({"error": "Please provide 'text' in JSON body"}), 400

#     text = data["text"]

#     # 1️⃣ BERT fake-news prediction
#     result = fake_news_detector(text)[0]
#     label = "FAKE" if result["label"] == "LABEL_1" else "REAL"
#     confidence = round(result["score"], 3)

#     # 2️⃣ FactCheck API
#     fact_result = fact_check(text)

#     # 3️⃣ Wikipedia fallback
#     wiki_result = wikipedia_check(text)

#     # ✅ Final combined JSON response
#     return jsonify({
#         "input_text": text,
#         "bert_label": label,
#         "bert_confidence": confidence,
#         "fact_verdict": fact_result["verified"],
#         "fact_source": fact_result["source"],
#         "fact_full_data": fact_result["full"],   # 👈 Added this back
#         "wiki_found": wiki_result["wiki_found"],
#         "wiki_summary": wiki_result["wiki_summary"],
#         "wiki_source": wiki_result["wiki_source"]
#     })

# # ===============================================
# # 🚀 Run the Server
# # ===============================================
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from huggingface_hub import login
import requests
import os
import wikipedia
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

# ===============================================
# 🔐 Load environment variables
# ===============================================
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
FACTCHECK_API_KEY = os.getenv("FACTCHECK_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "fake_news_db")

if not HF_TOKEN or not FACTCHECK_API_KEY or not MONGO_URI:
    raise ValueError("❌ Make sure HF_TOKEN, FACTCHECK_API_KEY, and MONGO_URI are set in .env")

login(token=HF_TOKEN)

# ===============================================
# 🧠 Load BERT Model
# ===============================================
MODEL_ID = "mrm8488/bert-tiny-finetuned-fake-news-detection"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, token=HF_TOKEN)
fake_news_detector = pipeline("text-classification", model=model, tokenizer=tokenizer)

# ===============================================
# 🌐 Flask App
# ===============================================
app = Flask(__name__)

# ===============================================
# 🔗 MongoDB Connection
# ===============================================
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
history_col = db.history

# ===============================================
# 🔍 FactCheck API
# ===============================================
def fact_check(text):
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {"query": text, "key": FACTCHECK_API_KEY}
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

# ===============================================
# 📚 Wikipedia Check
# ===============================================
def wikipedia_check(text):
    try:
        search_results = wikipedia.search(text)
        if not search_results:
            return {"wiki_found": False, "wiki_summary": None, "wiki_source": None}
        page_title = search_results[0]
        page = wikipedia.page(page_title)
        summary = page.summary[:600]
        url = page.url
        return {"wiki_found": True, "wiki_summary": summary, "wiki_source": url}
    except Exception as e:
        return {"wiki_found": False, "wiki_summary": str(e), "wiki_source": None}

# ===============================================
# 🧾 Prediction Endpoint
# ===============================================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if "text" not in data:
        return jsonify({"error": "Please provide 'text' in JSON body"}), 400
    text = data["text"]

    # BERT prediction
    result = fake_news_detector(text)[0]
    label = "FAKE" if result["label"] == "LABEL_1" else "REAL"
    confidence = round(result["score"], 3)

    # FactCheck
    fact_result = fact_check(text)

    # Wikipedia
    wiki_result = wikipedia_check(text)

    # Save to MongoDB
    history_col.insert_one({
        "text": text,
        "bert_label": label,
        "bert_confidence": confidence,
        "fact_verdict": fact_result["verified"],
        "fact_source": fact_result["source"],
        "wiki_found": wiki_result["wiki_found"],
        "wiki_summary": wiki_result["wiki_summary"],
        "wiki_source": wiki_result["wiki_source"],
        "timestamp": datetime.utcnow()
    })

    return jsonify({
        "input_text": text,
        "bert_label": label,
        "bert_confidence": confidence,
        "fact_verdict": fact_result["verified"],
        "fact_source": fact_result["source"],
        "fact_full_data": fact_result["full"],
        "wiki_found": wiki_result["wiki_found"],
        "wiki_summary": wiki_result["wiki_summary"],
        "wiki_source": wiki_result["wiki_source"]
    })

# ===============================================
# 🚀 Run Server
# ===============================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
