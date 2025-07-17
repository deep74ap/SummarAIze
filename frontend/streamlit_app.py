
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from summary import show_summary_page
from ask_questions import show_chat_page
from self_eval import show_evaluation_page

# Page config
st.set_page_config(
    page_title="SummarAIze",
    page_icon="📚",
    layout="wide"
)

# Modern custom CSS for responsiveness and accessibility
st.markdown("""
<style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', 'Arial', sans-serif;
        background: #f4f6fb;
    }
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        color: white;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 12px rgba(33,150,243,0.08);
    }
    .upload-box {
        border: 2px dashed #2196F3;
        border-radius: 12px;
        padding: 2rem 1rem;
        text-align: center;
        margin: 1.5rem 0;
        background: #fff;
        transition: border-color 0.3s;
    }
    .upload-box:focus-within {
        border-color: #4CAF50;
    }
    .mode-container {
        background: #fff;
        padding: 1.5rem 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.07);
        margin: 1.5rem 0;
    }
    .stRadio > div {
        justify-content: center;
        gap: 2rem;
    }
    @media (max-width: 768px) {
        .main-header { font-size: 1.1rem; padding: 1rem 0; }
        .upload-box, .mode-container { padding: 1rem 0.5rem; }
    }
</style>
""", unsafe_allow_html=True)


# Sidebar navigation for accessibility and easy navigation
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/artificial-intelligence.png", width=64)
    st.title("SummarAIze")
    st.markdown("""
    <small>AI-powered PDF Chat Assistant</small>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**Instructions:**\n- Upload a PDF\n- Choose a mode\n- Interact with your document!", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("[GitHub Repo](https://github.com/deep74ap/SummarAIze)")

# Main header
st.markdown("""
<div class="main-header" role="banner" aria-label="SummarAIze PDF Chat Assistant">
    <h1 style="margin-bottom:0.2em;">📚 SummarAIze</h1>
    <p style="margin-top:0;">Upload a PDF and start chatting with your document</p>
</div>
""", unsafe_allow_html=True)

# File upload section
st.markdown('<div class="upload-box" tabindex="0" aria-label="Upload PDF">', unsafe_allow_html=True)
st.markdown("### 📄 Upload Your PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", help="Only PDF files are supported.")
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    st.session_state.uploaded_file = uploaded_file
    st.success(f"✅ File uploaded: {uploaded_file.name}")

    # Show summary in an expander for better UX
    with st.expander("📑 View PDF Summary", expanded=True):
        show_summary_page(uploaded_file)

    # Mode selection in tabs for modern navigation
    st.markdown('<div class="mode-container">', unsafe_allow_html=True)
    tabs = st.tabs(["💬 Ask Questions", "📊 Self Evaluation"])
    with tabs[0]:
        st.markdown("### 💬 Ask Questions")
        show_chat_page()
    with tabs[1]:
        st.markdown("### 📊 Self Evaluation")
        show_evaluation_page()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("👆 Please upload a PDF file to get started!")
    st.markdown("---")
    # Feature highlights in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🤖 AI Chat")
        st.write("Ask questions about your PDF.")
    with col2:
        st.markdown("#### 📊 Analysis")
        st.write("Get document insights.")
    with col3:
        st.markdown("#### ⚡ Fast")
        st.write("Quick processing.")
        