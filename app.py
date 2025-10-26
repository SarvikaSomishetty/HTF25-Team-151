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
# # # # #                 st.subheader("🧠 AI Model (BERT) Prediction")
# # # # #                 st.write(f"**Prediction:** {data['bert_prediction']}")
# # # # #                 st.progress(data['bert_confidence'])
                
# # # # #                 st.subheader("🔎 Fact-Check Result")
# # # # #                 st.write(f"**Verdict:** {data['fact_verdict']}")
# # # # #                 st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

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
# # # # st.write("Analyze any news headline using AI + Google FactCheck API")

# # # # user_input = st.text_input("Enter a news headline or statement:")

# # # # if st.button("Analyze"):
# # # #     if not user_input.strip():
# # # #         st.warning("Please enter a news text first.")
# # # #     else:
# # # #         with st.spinner("Analyzing..."):
# # # #             response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
# # # #             if response.status_code == 200:
# # # #                 data = response.json()

# # # #                 # 🧠 BERT Prediction Section
# # # #                 st.subheader("🧠 AI Model (BERT) Prediction")
# # # #                 st.write(f"**BERT Label:** {data['bert_label']}")
# # # #                 st.write(f"**BERT Score:** {data['bert_score']:.4f}")
# # # #                 st.write(f"**Prediction:** {data['bert_prediction']}")
# # # #                 st.progress(data['bert_confidence'])

# # # #                 # 🔎 FactCheck Results
# # # #                 st.subheader("🔎 Fact-Check Result")
# # # #                 st.write(f"**Verdict:** {data['fact_verdict']}")
# # # #                 st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

# # # #                 # 🧩 Display any extra links from fact data
# # # #                 if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
# # # #                     for c in data["fact_full_data"]["claims"]:
# # # #                         if "claimReview" in c:
# # # #                             review = c["claimReview"][0]
# # # #                             st.markdown(f"[Read more here]({review.get('url', '#')})")
# # # #             else:
# # # #                 st.error("Error: Could not reach backend.")
# # # import streamlit as st
# # # import requests

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
# # #                     st.progress(min(data['bert_confidence'], 1.0))

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
# #                     # 🧠 BERT Prediction Section
# #                     # ============================================
# #                     st.subheader("🧠 AI Model (BERT) Prediction")
# #                     st.write(f"**Label:** {data['bert_label']}")
# #                     st.write(f"**Confidence:** {data['bert_confidence']:.3f}")

# #                     # 📊 Confidence Gauge (Plotly)
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

# #                     # ============================================
# #                     # 🧩 Smart Final Verdict
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

# #                 else:
# #                     st.error("❌ Error: Could not reach backend API.")
# #             except Exception as e:
# #                 st.error(f"⚠️ Request failed: {e}")
# import streamlit as st
# import requests
# import plotly.graph_objects as go

# st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# st.title("🧠 Fake News Detector")
# st.write("Analyze any news headline using **AI + Google FactCheck + Wikipedia** to verify authenticity.")

# # 📝 User Input
# user_input = st.text_input("Enter a news headline or statement:")

# if st.button("Analyze"):
#     if not user_input.strip():
#         st.warning("Please enter a news text first.")
#     else:
#         with st.spinner("Analyzing... please wait ⏳"):
#             try:
#                 response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
                
#                 if response.status_code == 200:
#                     data = response.json()

#                     # ============================================
#                     # 🧩 Smart Final Verdict — now on TOP
#                     # ============================================
#                     st.subheader("🏁 Final Verdict")

#                     label = data["bert_label"]
#                     conf = data["bert_confidence"]
#                     fact = str(data["fact_verdict"]).lower()
#                     wiki_found = data.get("wiki_found", False)

#                     if label == "REAL" and wiki_found:
#                         verdict = "✅ **Likely TRUE** — Supported by Wikipedia and AI confidence."
#                         color = "green"
#                     elif label == "FAKE" and ("false" in fact or "fake" in fact):
#                         verdict = "🚫 **Likely FAKE** — Both AI and FactCheck indicate falsehood."
#                         color = "red"
#                     elif conf > 0.8 and label == "REAL":
#                         verdict = "🟩 **Probably True** — High AI confidence, no conflicting sources."
#                         color = "green"
#                     elif conf > 0.8 and label == "FAKE":
#                         verdict = "🟥 **Probably Fake** — Strong AI fake detection, limited verification."
#                         color = "red"
#                     else:
#                         verdict = "⚠️ **Inconclusive** — Needs human review or more reliable data."
#                         color = "orange"

#                     st.markdown(f"<h3 style='color:{color}'>{verdict}</h3>", unsafe_allow_html=True)

#                     st.divider()

#                     # ============================================
#                     # 🧠 BERT Prediction Section
#                     # ============================================
#                     st.subheader("🧠 AI Model (BERT) Prediction")
#                     st.write(f"**Label:** {data['bert_label']}")
#                     st.write(f"**Confidence:** {data['bert_confidence']:.3f}")

#                     fig = go.Figure(go.Indicator(
#                         mode="gauge+number",
#                         value=data["bert_confidence"] * 100,
#                         title={"text": "AI Confidence (%)"},
#                         gauge={
#                             "axis": {"range": [0, 100]},
#                             "bar": {"color": "green" if data["bert_label"] == "REAL" else "red"},
#                             "steps": [
#                                 {"range": [0, 50], "color": "#ffcccc"},
#                                 {"range": [50, 75], "color": "#ffe0b3"},
#                                 {"range": [75, 100], "color": "#ccffcc"}
#                             ]
#                         }
#                     ))
#                     st.plotly_chart(fig, use_container_width=True)

#                     st.divider()

#                     # ============================================
#                     # 🔎 Google FactCheck Results
#                     # ============================================
#                     st.subheader("🔎 Google FactCheck Results")
#                     st.write(f"**Verdict:** {data['fact_verdict']}")
#                     st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

#                     if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
#                         st.markdown("**Related Fact-Check Articles:**")
#                         for claim in data["fact_full_data"]["claims"]:
#                             if "claimReview" in claim:
#                                 review = claim["claimReview"][0]
#                                 title = review.get("title", "Fact-check link")
#                                 url = review.get("url", "#")
#                                 st.markdown(f"- [{title}]({url})")

#                     st.divider()

#                     # ============================================
#                     # 📚 Wikipedia Knowledge Check
#                     # ============================================
#                     st.subheader("📚 Wikipedia Knowledge Check")
#                     if data.get("wiki_found"):
#                         if data["wiki_summary"]:
#                             st.write(data["wiki_summary"])
#                         if data["wiki_source"]:
#                             st.markdown(f"[🔗 Read more on Wikipedia]({data['wiki_source']})")
#                     else:
#                         st.info("No relevant Wikipedia article found for this claim.")

#                 else:
#                     st.error("❌ Error: Could not reach backend API.")
#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
import streamlit as st
import requests
import plotly.graph_objects as go
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# ===============================================
# 🔐 Load env
# ===============================================
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "fake_news_db")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
history_col = db.history

# ===============================================
# 🌟 Streamlit UI
# ===============================================
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")
st.title("🧠 Fake News Detector")
st.write("Analyze any news headline using **AI + Google FactCheck + Wikipedia** to verify authenticity.")

# Tabs for Analysis and History
tab1, tab2 = st.tabs(["Analyze News", "History"])

with tab1:
    user_input = st.text_input("Enter a news headline or statement:")

    if st.button("Analyze"):
        if not user_input.strip():
            st.warning("Please enter a news text first.")
        else:
            with st.spinner("Analyzing... please wait ⏳"):
                try:
                    response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
                    if response.status_code == 200:
                        data = response.json()

                        # ======================
                        # Final Verdict (TOP)
                        # ======================
                        st.subheader("🏁 Final Verdict")
                        label = data["bert_label"]
                        conf = data["bert_confidence"]
                        fact = str(data["fact_verdict"]).lower()
                        wiki_found = data.get("wiki_found", False)

                        if label == "REAL" and wiki_found:
                            verdict = "✅ **Likely TRUE** — Supported by Wikipedia and AI confidence."
                            color = "green"
                        elif label == "FAKE" and ("false" in fact or "fake" in fact):
                            verdict = "🚫 **Likely FAKE** — Both AI and FactCheck indicate falsehood."
                            color = "red"
                        elif conf > 0.8 and label == "REAL":
                            verdict = "🟩 **Probably True** — High AI confidence, no conflicting sources."
                            color = "green"
                        elif conf > 0.8 and label == "FAKE":
                            verdict = "🟥 **Probably Fake** — Strong AI fake detection, limited verification."
                            color = "red"
                        else:
                            verdict = "⚠️ **Inconclusive** — Needs human review or more reliable data."
                            color = "orange"

                        st.markdown(f"<h3 style='color:{color}'>{verdict}</h3>", unsafe_allow_html=True)
                        st.divider()

                        # ======================
                        # BERT Prediction
                        # ======================
                        st.subheader("🧠 AI Model (BERT) Prediction")
                        st.write(f"**Label:** {data['bert_label']}")
                        st.write(f"**Confidence:** {data['bert_confidence']:.3f}")

                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=data["bert_confidence"] * 100,
                            title={"text": "AI Confidence (%)"},
                            gauge={
                                "axis": {"range": [0, 100]},
                                "bar": {"color": "green" if data["bert_label"] == "REAL" else "red"},
                                "steps": [
                                    {"range": [0, 50], "color": "#ffcccc"},
                                    {"range": [50, 75], "color": "#ffe0b3"},
                                    {"range": [75, 100], "color": "#ccffcc"}
                                ]
                            }
                        ))
                        st.plotly_chart(fig, use_container_width=True)
                        st.divider()

                        # ======================
                        # FactCheck
                        # ======================
                        st.subheader("🔎 Google FactCheck Results")
                        st.write(f"**Verdict:** {data['fact_verdict']}")
                        st.write(f"**Source:** {data['fact_source'] or 'Not found'}")
                        if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
                            st.markdown("**Related Fact-Check Articles:**")
                            for claim in data["fact_full_data"]["claims"]:
                                if "claimReview" in claim:
                                    review = claim["claimReview"][0]
                                    title = review.get("title", "Fact-check link")
                                    url = review.get("url", "#")
                                    st.markdown(f"- [{title}]({url})")
                        st.divider()

                        # ======================
                        # Wikipedia
                        # ======================
                        st.subheader("📚 Wikipedia Knowledge Check")
                        if data.get("wiki_found"):
                            if data["wiki_summary"]:
                                st.write(data["wiki_summary"])
                            if data["wiki_source"]:
                                st.markdown(f"[🔗 Read more on Wikipedia]({data['wiki_source']})")
                        else:
                            st.info("No relevant Wikipedia article found for this claim.")

                    else:
                        st.error("❌ Error: Could not reach backend API.")
                except Exception as e:
                    st.error(f"⚠️ Request failed: {e}")

with tab2:
    st.subheader("🕒 Search History")
    history = list(history_col.find().sort("timestamp", -1).limit(50))
    for entry in history:
        st.markdown(f"**Text:** {entry['text']}")
        st.markdown(f"**AI Prediction:** {entry['bert_label']} ({entry['bert_confidence']})")
        st.markdown(f"**FactCheck:** {entry['fact_verdict']} ({entry.get('fact_source', 'N/A')})")
        st.markdown(f"**Wikipedia Found:** {entry['wiki_found']}")
        st.markdown(f"**Timestamp:** {entry['timestamp']}")
        st.divider()
