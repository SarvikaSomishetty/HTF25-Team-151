# # # # # # import streamlit as st
# # # # # # import requests

# # # # # # st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# # # # # # st.title("🧠 Fake News Detector")
# # # # # # st.write("Analyze any news headline using AI + Google FactCheck API")

# # # # # # user_input = st.text_input("Enter a news headline or statement:")

# # # # # # if st.button("Analyze"):
# # # # # #     if not user_input.strip():
# # # # # #         st.warning("Please enter a news text first.")
# # # # # #     else:
# # # # # #         with st.spinner("Analyzing..."):
# # # # # #             response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
# # # # # #             if response.status_code == 200:
# # # # # #                 data = response.json()
# # # # # #                 st.subheader("🧠 AI Model (BERT) Prediction")
# # # # # #                 st.write(f"**Prediction:** {data['bert_prediction']}")
# # # # # #                 st.progress(data['bert_confidence'])
                
# # # # # #                 st.subheader("🔎 Fact-Check Result")
# # # # # #                 st.write(f"**Verdict:** {data['fact_verdict']}")
# # # # # #                 st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

# # # # # #                 if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
# # # # # #                     for c in data["fact_full_data"]["claims"]:
# # # # # #                         if "claimReview" in c:
# # # # # #                             review = c["claimReview"][0]
# # # # # #                             st.markdown(f"[Read more here]({review.get('url', '#')})")
# # # # # #             else:
# # # # # #                 st.error("Error: Could not reach backend.")
# # # # # import streamlit as st
# # # # # import requests

# # # # # st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# # # # # st.title("🧠 Fake News Detector")
# # # # # st.write("Analyze any news headline using AI + Google FactCheck API")

# # # # # user_input = st.text_input("Enter a news headline or statement:")

# # # # # if st.button("Analyze"):
# # # # #     if not user_input.strip():
# # # # #         st.warning("Please enter a news text first.")
# # # # #     else:
# # # # #         with st.spinner("Analyzing..."):
# # # # #             response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
# # # # #             if response.status_code == 200:
# # # # #                 data = response.json()

# # # # #                 # 🧠 BERT Prediction Section
# # # # #                 st.subheader("🧠 AI Model (BERT) Prediction")
# # # # #                 st.write(f"**BERT Label:** {data['bert_label']}")
# # # # #                 st.write(f"**BERT Score:** {data['bert_score']:.4f}")
# # # # #                 st.write(f"**Prediction:** {data['bert_prediction']}")
# # # # #                 st.progress(data['bert_confidence'])

# # # # #                 # 🔎 FactCheck Results
# # # # #                 st.subheader("🔎 Fact-Check Result")
# # # # #                 st.write(f"**Verdict:** {data['fact_verdict']}")
# # # # #                 st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

# # # # #                 # 🧩 Display any extra links from fact data
# # # # #                 if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
# # # # #                     for c in data["fact_full_data"]["claims"]:
# # # # #                         if "claimReview" in c:
# # # # #                             review = c["claimReview"][0]
# # # # #                             st.markdown(f"[Read more here]({review.get('url', '#')})")
# # # # #             else:
# # # # #                 st.error("Error: Could not reach backend.")
# # # # import streamlit as st
# # # # import requests

# # # # st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# # # # st.title("🧠 Fake News Detector")
# # # # st.write("Analyze any news headline using **AI + Google FactCheck + Wikipedia** to verify authenticity.")

# # # # # 📝 User Input
# # # # user_input = st.text_input("Enter a news headline or statement:")

# # # # if st.button("Analyze"):
# # # #     if not user_input.strip():
# # # #         st.warning("Please enter a news text first.")
# # # #     else:
# # # #         with st.spinner("Analyzing... please wait ⏳"):
# # # #             try:
# # # #                 response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
                
# # # #                 if response.status_code == 200:
# # # #                     data = response.json()

# # # #                     # ============================================
# # # #                     # 🧠 BERT Prediction Section
# # # #                     # ============================================
# # # #                     st.subheader("🧠 AI Model (BERT) Prediction")
# # # #                     st.write(f"**Label:** {data['bert_label']}")
# # # #                     st.write(f"**Confidence:** {data['bert_confidence']:.3f}")
# # # #                     st.progress(min(data['bert_confidence'], 1.0))

# # # #                     # ============================================
# # # #                     # 🔎 Google FactCheck Results
# # # #                     # ============================================
# # # #                     st.subheader("🔎 Google FactCheck Results")
# # # #                     st.write(f"**Verdict:** {data['fact_verdict']}")
# # # #                     st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

# # # #                     if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
# # # #                         st.markdown("**Related Fact-Check Articles:**")
# # # #                         for claim in data["fact_full_data"]["claims"]:
# # # #                             if "claimReview" in claim:
# # # #                                 review = claim["claimReview"][0]
# # # #                                 title = review.get("title", "Fact-check link")
# # # #                                 url = review.get("url", "#")
# # # #                                 st.markdown(f"- [{title}]({url})")

# # # #                     # ============================================
# # # #                     # 📚 Wikipedia Knowledge Check
# # # #                     # ============================================
# # # #                     st.subheader("📚 Wikipedia Knowledge Check")
# # # #                     if data.get("wiki_found"):
# # # #                         if data["wiki_summary"]:
# # # #                             st.write(data["wiki_summary"])
# # # #                         if data["wiki_source"]:
# # # #                             st.markdown(f"[🔗 Read more on Wikipedia]({data['wiki_source']})")
# # # #                     else:
# # # #                         st.info("No relevant Wikipedia article found for this claim.")

# # # #                 else:
# # # #                     st.error("❌ Error: Could not reach backend API.")
# # # #             except Exception as e:
# # # #                 st.error(f"⚠️ Request failed: {e}")
# # # import streamlit as st
# # # import requests
# # # import plotly.graph_objects as go

# # # st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# # # st.title("🧠 Fake News Detector")
# # # st.write("Analyze any news headline using **AI + Google FactCheck + Wikipedia** to verify authenticity.")

# # # # 📝 User Input
# # # user_input = st.text_input("Enter a news headline or statement:")

# # # if st.button("Analyze"):
# # #     if not user_input.strip():
# # #         st.warning("Please enter a news text first.")
# # #     else:
# # #         with st.spinner("Analyzing... please wait ⏳"):
# # #             try:
# # #                 response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
                
# # #                 if response.status_code == 200:
# # #                     data = response.json()

# # #                     # ============================================
# # #                     # 🧠 BERT Prediction Section
# # #                     # ============================================
# # #                     st.subheader("🧠 AI Model (BERT) Prediction")
# # #                     st.write(f"**Label:** {data['bert_label']}")
# # #                     st.write(f"**Confidence:** {data['bert_confidence']:.3f}")

# # #                     # 📊 Confidence Gauge (Plotly)
# # #                     fig = go.Figure(go.Indicator(
# # #                         mode="gauge+number",
# # #                         value=data["bert_confidence"] * 100,
# # #                         title={"text": "AI Confidence (%)"},
# # #                         gauge={
# # #                             "axis": {"range": [0, 100]},
# # #                             "bar": {"color": "green" if data["bert_label"] == "REAL" else "red"},
# # #                             "steps": [
# # #                                 {"range": [0, 50], "color": "#ffcccc"},
# # #                                 {"range": [50, 75], "color": "#ffe0b3"},
# # #                                 {"range": [75, 100], "color": "#ccffcc"}
# # #                             ]
# # #                         }
# # #                     ))
# # #                     st.plotly_chart(fig, use_container_width=True)

# # #                     # ============================================
# # #                     # 🔎 Google FactCheck Results
# # #                     # ============================================
# # #                     st.subheader("🔎 Google FactCheck Results")
# # #                     st.write(f"**Verdict:** {data['fact_verdict']}")
# # #                     st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

# # #                     if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
# # #                         st.markdown("**Related Fact-Check Articles:**")
# # #                         for claim in data["fact_full_data"]["claims"]:
# # #                             if "claimReview" in claim:
# # #                                 review = claim["claimReview"][0]
# # #                                 title = review.get("title", "Fact-check link")
# # #                                 url = review.get("url", "#")
# # #                                 st.markdown(f"- [{title}]({url})")

# # #                     # ============================================
# # #                     # 📚 Wikipedia Knowledge Check
# # #                     # ============================================
# # #                     st.subheader("📚 Wikipedia Knowledge Check")
# # #                     if data.get("wiki_found"):
# # #                         if data["wiki_summary"]:
# # #                             st.write(data["wiki_summary"])
# # #                         if data["wiki_source"]:
# # #                             st.markdown(f"[🔗 Read more on Wikipedia]({data['wiki_source']})")
# # #                     else:
# # #                         st.info("No relevant Wikipedia article found for this claim.")

# # #                     # ============================================
# # #                     # 🧩 Smart Final Verdict
# # #                     # ============================================
# # #                     st.subheader("🏁 Final Verdict")

# # #                     label = data["bert_label"]
# # #                     conf = data["bert_confidence"]
# # #                     fact = str(data["fact_verdict"]).lower()
# # #                     wiki_found = data.get("wiki_found", False)

# # #                     if label == "REAL" and wiki_found:
# # #                         verdict = "✅ **Likely TRUE** — Supported by Wikipedia and AI confidence."
# # #                         color = "green"
# # #                     elif label == "FAKE" and ("false" in fact or "fake" in fact):
# # #                         verdict = "🚫 **Likely FAKE** — Both AI and FactCheck indicate falsehood."
# # #                         color = "red"
# # #                     elif conf > 0.8 and label == "REAL":
# # #                         verdict = "🟩 **Probably True** — High AI confidence, no conflicting sources."
# # #                         color = "green"
# # #                     elif conf > 0.8 and label == "FAKE":
# # #                         verdict = "🟥 **Probably Fake** — Strong AI fake detection, limited verification."
# # #                         color = "red"
# # #                     else:
# # #                         verdict = "⚠️ **Inconclusive** — Needs human review or more reliable data."
# # #                         color = "orange"

# # #                     st.markdown(f"<h3 style='color:{color}'>{verdict}</h3>", unsafe_allow_html=True)

# # #                 else:
# # #                     st.error("❌ Error: Could not reach backend API.")
# # #             except Exception as e:
# # #                 st.error(f"⚠️ Request failed: {e}")
# # import streamlit as st
# # import requests
# # import plotly.graph_objects as go

# # st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# # st.title("🧠 Fake News Detector")
# # st.write("Analyze any news headline using **AI + Google FactCheck + Wikipedia** to verify authenticity.")

# # # 📝 User Input
# # user_input = st.text_input("Enter a news headline or statement:")

# # if st.button("Analyze"):
# #     if not user_input.strip():
# #         st.warning("Please enter a news text first.")
# #     else:
# #         with st.spinner("Analyzing... please wait ⏳"):
# #             try:
# #                 response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
                
# #                 if response.status_code == 200:
# #                     data = response.json()

# #                     # ============================================
# #                     # 🧩 Smart Final Verdict — now on TOP
# #                     # ============================================
# #                     st.subheader("🏁 Final Verdict")

# #                     label = data["bert_label"]
# #                     conf = data["bert_confidence"]
# #                     fact = str(data["fact_verdict"]).lower()
# #                     wiki_found = data.get("wiki_found", False)

# #                     if label == "REAL" and wiki_found:
# #                         verdict = "✅ **Likely TRUE** — Supported by Wikipedia and AI confidence."
# #                         color = "green"
# #                     elif label == "FAKE" and ("false" in fact or "fake" in fact):
# #                         verdict = "🚫 **Likely FAKE** — Both AI and FactCheck indicate falsehood."
# #                         color = "red"
# #                     elif conf > 0.8 and label == "REAL":
# #                         verdict = "🟩 **Probably True** — High AI confidence, no conflicting sources."
# #                         color = "green"
# #                     elif conf > 0.8 and label == "FAKE":
# #                         verdict = "🟥 **Probably Fake** — Strong AI fake detection, limited verification."
# #                         color = "red"
# #                     else:
# #                         verdict = "⚠️ **Inconclusive** — Needs human review or more reliable data."
# #                         color = "orange"

# #                     st.markdown(f"<h3 style='color:{color}'>{verdict}</h3>", unsafe_allow_html=True)

# #                     st.divider()

# #                     # ============================================
# #                     # 🧠 BERT Prediction Section
# #                     # ============================================
# #                     st.subheader("🧠 AI Model (BERT) Prediction")
# #                     st.write(f"**Label:** {data['bert_label']}")
# #                     st.write(f"**Confidence:** {data['bert_confidence']:.3f}")

# #                     fig = go.Figure(go.Indicator(
# #                         mode="gauge+number",
# #                         value=data["bert_confidence"] * 100,
# #                         title={"text": "AI Confidence (%)"},
# #                         gauge={
# #                             "axis": {"range": [0, 100]},
# #                             "bar": {"color": "green" if data["bert_label"] == "REAL" else "red"},
# #                             "steps": [
# #                                 {"range": [0, 50], "color": "#ffcccc"},
# #                                 {"range": [50, 75], "color": "#ffe0b3"},
# #                                 {"range": [75, 100], "color": "#ccffcc"}
# #                             ]
# #                         }
# #                     ))
# #                     st.plotly_chart(fig, use_container_width=True)

# #                     st.divider()

# #                     # ============================================
# #                     # 🔎 Google FactCheck Results
# #                     # ============================================
# #                     st.subheader("🔎 Google FactCheck Results")
# #                     st.write(f"**Verdict:** {data['fact_verdict']}")
# #                     st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

# #                     if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
# #                         st.markdown("**Related Fact-Check Articles:**")
# #                         for claim in data["fact_full_data"]["claims"]:
# #                             if "claimReview" in claim:
# #                                 review = claim["claimReview"][0]
# #                                 title = review.get("title", "Fact-check link")
# #                                 url = review.get("url", "#")
# #                                 st.markdown(f"- [{title}]({url})")

# #                     st.divider()

# #                     # ============================================
# #                     # 📚 Wikipedia Knowledge Check
# #                     # ============================================
# #                     st.subheader("📚 Wikipedia Knowledge Check")
# #                     if data.get("wiki_found"):
# #                         if data["wiki_summary"]:
# #                             st.write(data["wiki_summary"])
# #                         if data["wiki_source"]:
# #                             st.markdown(f"[🔗 Read more on Wikipedia]({data['wiki_source']})")
# #                     else:
# #                         st.info("No relevant Wikipedia article found for this claim.")

# #                 else:
# #                     st.error("❌ Error: Could not reach backend API.")
# #             except Exception as e:
# #                 st.error(f"⚠️ Request failed: {e}")
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv

# # ===============================================
# # 🔐 Load env
# # ===============================================
# load_dotenv()
# MONGO_URI = os.getenv("MONGO_URI")
# DB_NAME = os.getenv("DB_NAME", "fake_news_db")

# client = MongoClient(MONGO_URI)
# db = client[DB_NAME]
# history_col = db.history

# # ===============================================
# # 🌟 Streamlit UI
# # ===============================================
# st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")
# st.title("🧠 Fake News Detector")
# st.write("Analyze any news headline using **AI + Google FactCheck + Wikipedia** to verify authenticity.")

# # Tabs for Analysis and History
# tab1, tab2 = st.tabs(["Analyze News", "History"])

# with tab1:
#     user_input = st.text_input("Enter a news headline or statement:")

#     if st.button("Analyze"):
#         if not user_input.strip():
#             st.warning("Please enter a news text first.")
#         else:
#             with st.spinner("Analyzing... please wait ⏳"):
#                 try:
#                     response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
#                     if response.status_code == 200:
#                         data = response.json()

#                         # ======================
#                         # Final Verdict (TOP)
#                         # ======================
#                         st.subheader("🏁 Final Verdict")
#                         label = data["bert_label"]
#                         conf = data["bert_confidence"]
#                         fact = str(data["fact_verdict"]).lower()
#                         wiki_found = data.get("wiki_found", False)

#                         if label == "REAL" and wiki_found:
#                             verdict = "✅ **Likely TRUE** — Supported by Wikipedia and AI confidence."
#                             color = "green"
#                         elif label == "FAKE" and ("false" in fact or "fake" in fact):
#                             verdict = "🚫 **Likely FAKE** — Both AI and FactCheck indicate falsehood."
#                             color = "red"
#                         elif conf > 0.8 and label == "REAL":
#                             verdict = "🟩 **Probably True** — High AI confidence, no conflicting sources."
#                             color = "green"
#                         elif conf > 0.8 and label == "FAKE":
#                             verdict = "🟥 **Probably Fake** — Strong AI fake detection, limited verification."
#                             color = "red"
#                         else:
#                             verdict = "⚠️ **Inconclusive** — Needs human review or more reliable data."
#                             color = "orange"

#                         st.markdown(f"<h3 style='color:{color}'>{verdict}</h3>", unsafe_allow_html=True)
#                         st.divider()

#                         # ======================
#                         # BERT Prediction
#                         # ======================
#                         st.subheader("🧠 AI Model (BERT) Prediction")
#                         st.write(f"**Label:** {data['bert_label']}")
#                         st.write(f"**Confidence:** {data['bert_confidence']:.3f}")

#                         fig = go.Figure(go.Indicator(
#                             mode="gauge+number",
#                             value=data["bert_confidence"] * 100,
#                             title={"text": "AI Confidence (%)"},
#                             gauge={
#                                 "axis": {"range": [0, 100]},
#                                 "bar": {"color": "green" if data["bert_label"] == "REAL" else "red"},
#                                 "steps": [
#                                     {"range": [0, 50], "color": "#ffcccc"},
#                                     {"range": [50, 75], "color": "#ffe0b3"},
#                                     {"range": [75, 100], "color": "#ccffcc"}
#                                 ]
#                             }
#                         ))
#                         st.plotly_chart(fig, use_container_width=True)
#                         st.divider()

#                         # ======================
#                         # FactCheck
#                         # ======================
#                         st.subheader("🔎 Google FactCheck Results")
#                         st.write(f"**Verdict:** {data['fact_verdict']}")
#                         st.write(f"**Source:** {data['fact_source'] or 'Not found'}")
#                         if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
#                             st.markdown("**Related Fact-Check Articles:**")
#                             for claim in data["fact_full_data"]["claims"]:
#                                 if "claimReview" in claim:
#                                     review = claim["claimReview"][0]
#                                     title = review.get("title", "Fact-check link")
#                                     url = review.get("url", "#")
#                                     st.markdown(f"- [{title}]({url})")
#                         st.divider()

#                         # ======================
#                         # Wikipedia
#                         # ======================
#                         st.subheader("📚 Wikipedia Knowledge Check")
#                         if data.get("wiki_found"):
#                             if data["wiki_summary"]:
#                                 st.write(data["wiki_summary"])
#                             if data["wiki_source"]:
#                                 st.markdown(f"[🔗 Read more on Wikipedia]({data['wiki_source']})")
#                         else:
#                             st.info("No relevant Wikipedia article found for this claim.")

#                     else:
#                         st.error("❌ Error: Could not reach backend API.")
#                 except Exception as e:
#                     st.error(f"⚠️ Request failed: {e}")

# with tab2:
#     st.subheader("🕒 Search History")
#     history = list(history_col.find().sort("timestamp", -1).limit(50))
#     for entry in history:
#         st.markdown(f"**Text:** {entry['text']}")
#         st.markdown(f"**AI Prediction:** {entry['bert_label']} ({entry['bert_confidence']})")
#         st.markdown(f"**FactCheck:** {entry['fact_verdict']} ({entry.get('fact_source', 'N/A')})")
#         st.markdown(f"**Wikipedia Found:** {entry['wiki_found']}")
#         st.markdown(f"**Timestamp:** {entry['timestamp']}")
#         st.divider()
from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer, AutoModel
from huggingface_hub import login
import requests
import os
import wikipedia
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

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
# 🧠 Load BERT Model (Existing)
# ===============================================
MODEL_ID = "mrm8488/bert-tiny-finetuned-fake-news-detection"
tokenizer_bert = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
model_bert = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, token=HF_TOKEN)
fake_news_detector = pipeline("text-classification", model=model_bert, tokenizer=tokenizer_bert)

# ===============================================
# 🔥 Load Custom BERT-CNN Model
# ===============================================
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PATH = "bert_cnn_fakenews.pth"

# Custom Model Definition
class BERT_CNN_Metadata_Classifier(nn.Module):
    def _init_(self, bert_model_name="distilbert-base-uncased",
                 cnn_out_channels=256, kernel_sizes=[2,3,4,5],
                 num_classes=5, dropout=0.3, metadata_emb_dim=16,
                 num_speakers=None, num_parties=None, num_venues=None):
        super()._init_()
        self.bert = AutoModel.from_pretrained(bert_model_name)
        self.convs = nn.ModuleList([
            nn.Conv1d(self.bert.config.hidden_size, cnn_out_channels, k) for k in kernel_sizes
        ])
        self.dropout = nn.Dropout(dropout)
        self.speaker_emb = nn.Embedding(num_speakers, metadata_emb_dim)
        self.party_emb   = nn.Embedding(num_parties, metadata_emb_dim)
        self.venue_emb   = nn.Embedding(num_venues, metadata_emb_dim)
        total_features = self.bert.config.hidden_size + cnn_out_channels * len(kernel_sizes) + metadata_emb_dim*3
        self.fc = nn.Linear(total_features, num_classes)

    def forward(self, input_ids, attention_mask, metadata_ids):
        bert_out = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        cls_emb = bert_out.last_hidden_state[:,0]
        x = bert_out.last_hidden_state.transpose(1,2)
        cnn_outs = [F.relu(conv(x)) for conv in self.convs]
        cnn_pooled = [F.max_pool1d(o, o.size(2)).squeeze(2) for o in cnn_outs]
        cnn_feat = torch.cat(cnn_pooled, dim=1)
        speaker_emb = self.speaker_emb(metadata_ids[:,0])
        party_emb   = self.party_emb(metadata_ids[:,1])
        venue_emb   = self.venue_emb(metadata_ids[:,2])
        metadata_feat = torch.cat([speaker_emb, party_emb, venue_emb], dim=1)
        combined = torch.cat([cls_emb, cnn_feat, metadata_feat], dim=1)
        out = self.fc(self.dropout(combined))
        return out

# Load Custom Model
MODEL_NAME = "distilbert-base-uncased"
tokenizer_custom = AutoTokenizer.from_pretrained(MODEL_NAME)

custom_model = BERT_CNN_Metadata_Classifier(
    num_speakers=2911,
    num_parties=24,
    num_venues=4346,
    num_classes=5
).to(DEVICE)

custom_model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
custom_model.eval()

# ===============================================
# 🌐 Flask App
# ===============================================
app = Flask(_name_)

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
# 🧾 EXISTING MODEL: /predict
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
        "model_type": "BERT_HuggingFace",
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
        "model_type": "BERT_HuggingFace",
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
# 🔥 CUSTOM MODEL: /predict_custom
# ===============================================
@app.route("/predict_custom", methods=["POST"])
def predict_custom():
    data = request.json
    if "text" not in data:
        return jsonify({"error": "Please provide 'text' in JSON body"}), 400
    
    text = data["text"]
    
    # Use default metadata (unknown speaker/party/venue)
    metadata_vec = [0, 0, 0]  # Default IDs
    
    # Tokenize
    tokens = tokenizer_custom([text], padding=True, truncation=True, 
                             return_tensors="pt", max_length=128)
    input_ids = tokens['input_ids'].to(DEVICE)
    attention_mask = tokens['attention_mask'].to(DEVICE)
    metadata = torch.tensor([metadata_vec], dtype=torch.long).to(DEVICE)
    
    # Predict
    with torch.no_grad():
        logits = custom_model(input_ids, attention_mask, metadata)
        probs = torch.softmax(logits, dim=1)
        pred_class = torch.argmax(probs, dim=1).item()
        confidence = float(probs[0][pred_class])
    
    # Map to labels
    labels = ["TRUE", "MOSTLY-TRUE", "HALF-TRUE", "BARELY-TRUE", "FAKE"]
    pred_label = labels[pred_class]
    
    # Simplified label for consistency
    simplified_label = "REAL" if pred_class < 3 else "FAKE"
    
    # FactCheck (optional - you can keep or remove)
    fact_result = fact_check(text)
    
    # Save to MongoDB
    history_col.insert_one({
        "text": text,
        "model_type": "Custom_BERT_CNN",
        "bert_label": simplified_label,
        "detailed_label": pred_label,
        "bert_confidence": confidence,
        "fact_verdict": fact_result["verified"],
        "fact_source": fact_result["source"],
        "timestamp": datetime.utcnow()
    })
    
    return jsonify({
        "model_type": "Custom_BERT_CNN",
        "input_text": text,
        "bert_label": simplified_label,
        "detailed_label": pred_label,
        "bert_confidence": confidence,
        "fact_verdict": fact_result["verified"],
        "fact_source": fact_result["source"],
        "fact_full_data": fact_result["full"]
    })

# ===============================================
# 🚀 Run Server
# ===============================================
if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)