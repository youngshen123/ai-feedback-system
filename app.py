import streamlit as st
from analysis import analyze_feedback
from report import generate_report

st.title("AI Student Feedback Analyzer")

df = analyze_feedback("data/feedback.csv")

st.write(df)

if st.button("Generate AI Report"):
    text = " ".join(df['feedback'].tolist())
    report = generate_report(text)
    st.write(report)