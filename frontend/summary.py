
import os
import streamlit as st
from backend.vector_database import upload_pdf, build_faiss_index, load_pdf
from backend.rag_pipeline import summarize_doc, load_faiss_db


def show_summary_page(uploaded_file):
    os.makedirs("pdfs", exist_ok=True)
    upload_pdf(uploaded_file)
    file_path = "pdfs/" + uploaded_file.name

    build_faiss_index([file_path])
    faiss_db = load_faiss_db()

    documents = load_pdf(file_path)
    summary = summarize_doc(documents)

    
    st.subheader(" Document Summary")
    st.markdown(summary)

    
    st.session_state["faiss_db"] = faiss_db
    st.session_state["documents"] = documents
