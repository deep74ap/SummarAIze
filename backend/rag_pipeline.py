import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())

FAISS_DB_PATH = "vectorstore/db_faiss"

# Initialize Groq model
llm_model = ChatGroq(model="deepseek-r1-distill-llama-70b")

# from langchain_core.prompts import ChatPromptTemplate

def summarize_doc(documents, model=llm_model, word_limit=3000):
    context = get_context(documents)

    # Truncate context to first 3000 words
    context_words = context.split()
    trimmed_context = " ".join(context_words[:word_limit])

    prompt = ChatPromptTemplate.from_template("""
Summarize the following document in approximately 150 words.

{context}

Summary:
""")

    chain = prompt | model
    return chain.invoke({"context": trimmed_context}).content.strip()


def generate_questions(documents, model):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(f"""
    You are a quiz creator. Based on the following context, generate 3 clear, short, and relevant quiz questions.
    
    Format them as:
    Q1: ...
    Q2: ...
    Q3: ...

    Only output the questions. Do not explain or think aloud.

    Context:
    {context}
    """)
    chain = prompt | model
    response = chain.invoke({"context": context}).content.strip()
    return [q.strip() for q in response.splitlines() if q.strip().startswith("Q")]


def evaluate_answer(question, user_answer, context, model, source_doc=None):
    prompt = ChatPromptTemplate.from_template("""
Evaluate the user's answer based strictly on the context provided.

Always follow this structured format:

 **Thinking (max 50 words)**: <How you assessed the answer>  
 **Score (out of 10)**: <Score>  
 **Justification**: Quote or describe the part of the context that supports or challenges the answer. Mention page and paragraph if possible.

Question: {question}  
User's Answer: {user_answer}  
 

Evaluation:
""")

    chain = prompt | model
    result = chain.invoke({
        "question": question,
        "user_answer": user_answer,
        "context": context
    }).content.strip()

    if source_doc:
        metadata = source_doc.metadata
        source = metadata.get("source", "Unknown")
        page = metadata.get("page", "?")
        paragraph = metadata.get("paragraph", "?")
        result += f"\n **Source:** `{source}` (Page {page}, Paragraph {paragraph})"
    else:
        result += "\n **Source:** Not found."

    return result



def load_faiss_db(db_path=FAISS_DB_PATH):
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(db_path, embedding_model, allow_dangerous_deserialization=True)

def retrieve_docs(faiss_db, query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context

custom_prompt_template = custom_prompt_template = """
You're an assistant helping answer questions based only on the provided context.

Always follow this format:
1.  **Thinking (max 50 words)**: <your short reasoning do not think in more than 50 words>
2.  **Answer**: <your final answer>
3.  **Justification**: Quote or summarize which part of the context helped, including paragraph and page number if mentioned.

Question: {question} 
Context: {context} 
Response:
"""




def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    response = chain.invoke({"question": query, "context": context})
    return response.content  # ✅ Only return the text, not the metadata





