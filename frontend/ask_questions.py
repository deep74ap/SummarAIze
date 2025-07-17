import streamlit as st
from backend.rag_pipeline import retrieve_docs, answer_query, llm_model


def show_chat_page():
    # Display formatted response
    


    st.subheader("Ask Questions About the Document")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Improved search bar style
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input(
            "Ask your question here...",
            key="chat_input",
            placeholder="Type your question and press Enter or click Send",
            help="Type your question about the PDF document."
        )
        submit = st.form_submit_button("Send", use_container_width=True)

    if submit and user_input:
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
        st.session_state.chat_history.append({"role": "ai", "content": final_response})

    # Display chat history only (prevents double printing)
    import re
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            content = msg["content"]
            if msg["role"] == "ai":
                # Remove and ignore <think> section for now (not rendered)
                content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()

                # Extract Answer, Justification, Source
                answer_match = re.search(r'\*\*Answer:?\*\*(.*?)(\*\*Justification|\*\*Source|$)', content, re.DOTALL)
                justification_match = re.search(r'\*\*Justification\*\*:?(.+?)(\*\*Source|$)', content, re.DOTALL)
                source_match = re.search(r'\*\*Source:?\*\*(.+)', content, re.DOTALL)

                # Render Answer
                if answer_match:
                    answer_text = answer_match.group(1).strip().lstrip(':').strip()
                    if answer_text:
                        st.markdown(f'<div style="background:#e8f5e9;padding:0.7em 1em;border-radius:8px;margin-bottom:0.5em;color:#256029;"><b>📝 Answer:</b> {answer_text}</div>', unsafe_allow_html=True)

                # Render Justification
                if justification_match:
                    justification_text = justification_match.group(1).strip().lstrip(':').strip()
                    if justification_text:
                        st.markdown(f'<div style="background:#fff3e0;padding:0.7em 1em;border-radius:8px;margin-bottom:0.5em;"><b>🟠 Justification:</b> {justification_text}</div>', unsafe_allow_html=True)

                # Render Source
                if source_match:
                    source_text = source_match.group(1).strip().lstrip(':').strip()
                    if source_text:
                        st.markdown(f'<div style="background:#f1f8e9;padding:0.7em 1em;border-radius:8px;margin-bottom:0.5em;"><b>📄 Source:</b> {source_text}</div>', unsafe_allow_html=True)
            else:
                st.markdown(content)
