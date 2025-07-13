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
    layout="centered"
)

# Simple custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .upload-box {
        border: 2px dashed #4CAF50;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
        background: #f8f9fa;
    }
    
    .mode-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .stRadio > div {
        justify-content: center;
        gap: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>📚 SummarAIze : PDF Chat Assistant</h1>
    <p>Upload a PDF and start chatting with your document</p>
</div>
""", unsafe_allow_html=True)

# File upload
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
st.markdown("### 📄 Upload Your PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    st.session_state.uploaded_file = uploaded_file
    st.success(f"✅ File uploaded: {uploaded_file.name}")
    
    # Show summary
    show_summary_page(uploaded_file)
    
    # Mode selection
    st.markdown('<div class="mode-container">', unsafe_allow_html=True)
    st.markdown("### Choose Mode")
    mode = st.radio(
        "Select what you want to do:",
        ["Ask Questions", "Self Evaluation"],
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show selected mode
    if mode == "Ask Questions":
        st.markdown("---")
        st.markdown("### 💬 Ask Questions")
        show_chat_page()
    elif mode == "Self Evaluation":
        st.markdown("---")
        st.markdown("### 📊 Self Evaluation")
        show_evaluation_page()

else:
    st.info("👆 Please upload a PDF file to get started!")
    
    # Simple features
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🤖 AI Chat")
        st.write("Ask questions about your PDF")
    
    with col2:
        st.markdown("### 📊 Analysis")
        st.write("Get document insights")
    
    with col3:
        st.markdown("### ⚡ Fast")
        st.write("Quick processing")
        