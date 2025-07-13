
import streamlit as st
from backend.rag_pipeline import generate_questions, evaluate_answer, llm_model, get_context

def show_evaluation_page():
    st.subheader(" Self Evaluation Quiz")

    documents = st.session_state.get("documents")
    if not documents:
        st.error("Document not loaded. Please upload a PDF first.")
        return

    context = get_context(documents)

    if "quiz_questions" not in st.session_state:
        with st.spinner("Generating questions..."):
            questions = generate_questions(documents, llm_model)
            st.session_state.quiz_questions = [q for q in questions if q.strip()]

    submitted = False
    answers = []

    with st.form("quiz_form"):
        for i, question in enumerate(st.session_state.quiz_questions):
            st.markdown(f"**Q{i+1}:** {question}")
            answer = st.text_area(f"Your Answer {i+1}", key=f"answer_{i}", height=100)
            answers.append(answer)
        submitted = st.form_submit_button("Submit Answers")

    if submitted:
        st.subheader(" Evaluation Results")
        for i, (q, user_ans) in enumerate(zip(st.session_state.quiz_questions, answers)):
            with st.spinner(f"Evaluating Q{i+1}..."):
                doc_chunks = st.session_state.get("faiss_db").similarity_search(q)
                top_doc = doc_chunks[0] if doc_chunks else None
                feedback = evaluate_answer(q, user_ans, context, llm_model, source_doc=top_doc)
                st.markdown(f"**Q{i+1}:** {q}")
                st.markdown(feedback)
