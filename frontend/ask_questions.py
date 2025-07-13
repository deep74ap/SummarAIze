import streamlit as st
from backend.rag_pipeline import retrieve_docs, answer_query, llm_model


def show_chat_page():
    # Display formatted response
    


    st.subheader(" Ask Questions About the Document")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask your question here...")

    if user_input:
        st.chat_message("user").write(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        faiss_db = st.session_state.get("faiss_db")
        docs = retrieve_docs(faiss_db, user_input)
        answer = answer_query(docs, llm_model, user_input)

        if docs:
            metadata = docs[0].metadata
            source = metadata.get("source", "Unknown")
            page = metadata.get("page", "?")
            source_info = f"\n\n **Source:** `{source}` (Page {page})"
        else:
            source_info = "\n\n **Source:** Not found in document."

        final_response = answer + source_info

        st.chat_message("ai").write(final_response)
        st.session_state.chat_history.append({"role": "ai", "content": final_response})


    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
