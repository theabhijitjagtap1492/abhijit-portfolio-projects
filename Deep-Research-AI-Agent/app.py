import streamlit as st
from dotenv import load_dotenv, find_dotenv
from graph_runner import run_langgraph_pipeline  # pipeline logic
import os

# Loading .env variables (important for API keys)
load_dotenv(find_dotenv())

st.set_page_config(page_title="AI Research Agent", layout="wide")
st.title("🧠 Deep Research AI Agent")

# Text input from user i.e. query
user_query = st.text_input("Enter your research question or URL", "")

# Button triggers the LangGraph pipeline
if st.button("Run Research"):
    if user_query.strip():
        try:
            with st.spinner("Running agents..."):
                answer = run_langgraph_pipeline(user_query)
            st.markdown("### ✅ Final Answer")
            st.write(answer)
        except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a valid query or URL.")