import streamlit as st
from matcher import get_resume_match_score
from prompts import generate_feedback

st.title("📄 Resume & JD Matcher")

res_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
jd_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")

if res_file and jd_file:
    from io import BytesIO
    import fitz
    def extract(file):
        text = ""
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text
    
    resume_text = extract(res_file)
    jd_text = extract(jd_file)

    st.subheader("💬 Detailed Feedback")
    feedback = generate_feedback(resume_text, jd_text)
    st.markdown(feedback)
