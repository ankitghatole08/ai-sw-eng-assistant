import requests
import streamlit as st

st.set_page_config(
    page_title="AI Software Delivery Assistant",
    page_icon="🤖",
    layout="wide",
)

API_URL = "http://127.0.0.1:8000"

st.title("🤖 AI Software Delivery Assistant")
st.caption("GitHub Pull Request AI Reviewer powered by Gemini")

st.divider()

repo = st.text_input(
    "GitHub Repository",
    placeholder="https://github.com/psf/requests",
)

pr = st.number_input(
    "Pull Request Number",
    min_value=1,
    value=6940,
)

if st.button("🚀 Analyze Pull Request", use_container_width=True):

    if repo.strip() == "":
        st.warning("Please enter a repository URL.")
        st.stop()

    payload = {
        "repository_url": repo,
        "pull_request_number": int(pr),
    }

    with st.spinner("Analyzing Pull Request..."):

        try:

            response = requests.post(
                f"{API_URL}/review/pull-request",
                json=payload,
                timeout=180,
            )

            if response.status_code != 200:
                st.error(response.text)
                st.stop()

            data = response.json()

        except Exception as e:
            st.error(str(e))
            st.stop()

    st.success("Analysis Complete!")

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Overall Score",
            data["overall_score"],
        )

    with c2:
        st.metric(
            "Files Reviewed",
            len(data["files"]),
        )

    st.write(data["summary"])

    st.divider()

    for file in data["files"]:

        with st.expander(
            f"📄 {file['filename']}",
            expanded=False,
        ):

            st.markdown(
                f"**Status:** {file['status']}"
            )

            st.markdown("### AI Review")

            st.markdown(file["review"])