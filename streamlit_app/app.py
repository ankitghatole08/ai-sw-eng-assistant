import streamlit as st
import requests

st.set_page_config(
    page_title="AI Software Delivery Assistant",
    layout="wide"
)

st.title("🚀 AI Software Delivery Assistant")
st.subheader("GitHub PR → AI Code Review")

API_BASE_URL = "http://127.0.0.1:8000"

repo_url = st.text_input("GitHub Repository URL")
pr_number = st.number_input("Pull Request Number", min_value=1, step=1)

if st.button("Analyze Pull Request"):

    if not repo_url:
        st.error("Please enter repository URL")
        st.stop()

    payload = {
        "repository_url": repo_url,
        "pull_request_number": int(pr_number)
    }

    with st.spinner("Analyzing PR with AI..."):

        try:
            response = requests.post(
                f"{API_BASE_URL}/review/pull-request",
                json=payload,
                timeout=60
            )

            data = response.json()

        except Exception as e:
            st.error(f"Request failed: {str(e)}")
            st.stop()

    # -----------------------------
    # SAFETY CHECK (IMPORTANT FIX)
    # -----------------------------
    if not isinstance(data, dict):
        st.error("Invalid response from backend")
        st.write(data)
        st.stop()

    st.success("Analysis Complete!")

    # -----------------------------
    # SUMMARY
    # -----------------------------
    st.header("📊 Summary")

    st.metric(
        "Overall Score",
        data.get("overall_score", 0)
    )

    st.write(data.get("summary", "No summary returned"))

    # -----------------------------
    # FILE REVIEWS
    # -----------------------------
    st.header("📁 File Reviews")

    for file in data.get("files", []):

        with st.expander(f"📄 {file.get('filename', 'unknown')}"):

            st.write("### Review")
            st.write(file.get("review", "No review generated"))

            st.write("### Status")
            st.write(file.get("status", "unknown"))