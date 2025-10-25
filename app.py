# import streamlit as st
# import requests

# st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# st.title("🧠 Fake News Detector")
# st.write("Analyze any news headline using AI + Google FactCheck API")

# user_input = st.text_input("Enter a news headline or statement:")

# if st.button("Analyze"):
#     if not user_input.strip():
#         st.warning("Please enter a news text first.")
#     else:
#         with st.spinner("Analyzing..."):
#             response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
#             if response.status_code == 200:
#                 data = response.json()
#                 st.subheader("🧠 AI Model (BERT) Prediction")
#                 st.write(f"**Prediction:** {data['bert_prediction']}")
#                 st.progress(data['bert_confidence'])
                
#                 st.subheader("🔎 Fact-Check Result")
#                 st.write(f"**Verdict:** {data['fact_verdict']}")
#                 st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

#                 if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
#                     for c in data["fact_full_data"]["claims"]:
#                         if "claimReview" in c:
#                             review = c["claimReview"][0]
#                             st.markdown(f"[Read more here]({review.get('url', '#')})")
#             else:
#                 st.error("Error: Could not reach backend.")
import streamlit as st
import requests

st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

st.title("🧠 Fake News Detector")
st.write("Analyze any news headline using AI + Google FactCheck API")

user_input = st.text_input("Enter a news headline or statement:")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter a news text first.")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
            if response.status_code == 200:
                data = response.json()

                # 🧠 BERT Prediction Section
                st.subheader("🧠 AI Model (BERT) Prediction")
                st.write(f"**BERT Label:** {data['bert_label']}")
                st.write(f"**BERT Score:** {data['bert_score']:.4f}")
                st.write(f"**Prediction:** {data['bert_prediction']}")
                st.progress(data['bert_confidence'])

                # 🔎 FactCheck Results
                st.subheader("🔎 Fact-Check Result")
                st.write(f"**Verdict:** {data['fact_verdict']}")
                st.write(f"**Source:** {data['fact_source'] or 'Not found'}")

                # 🧩 Display any extra links from fact data
                if data.get("fact_full_data") and "claims" in data["fact_full_data"]:
                    for c in data["fact_full_data"]["claims"]:
                        if "claimReview" in c:
                            review = c["claimReview"][0]
                            st.markdown(f"[Read more here]({review.get('url', '#')})")
            else:
                st.error("Error: Could not reach backend.")
