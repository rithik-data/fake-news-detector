import streamlit as st
from model import predict_news

st.title("📰 Fake News Detector")

user_input = st.text_area("Enter News Text")

if st.button("Check"):
    if user_input:
        prediction, confidence = predict_news(user_input)

        if prediction == "FAKE":
            st.error(f"Fake News ❌ (Confidence: {confidence:.2f})")
        else:
            st.success(f"Real News ✅ (Confidence: {confidence:.2f})")
    else:
        st.warning("Please enter text")
