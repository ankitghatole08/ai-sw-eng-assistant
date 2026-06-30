import streamlit as st

st.set_page_config(
    page_title="AI Software Engineering Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Software Engineering Assistant")

st.success("Project setup completed successfully!")

st.write(
    """
    Welcome!

    This application will eventually support:

    - AI Pull Request Review
    - Test Generation
    - Release Notes
    - GitHub Integration
    - MCP Tool Calling
    """
)