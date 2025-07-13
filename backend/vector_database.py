

    
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

path_directory = 'pdfs/'

def upload_pdf(file):
    with open(path_directory + file.name, "wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    for i, doc in enumerate(documents):
        doc.metadata["source"] = file_path
        doc.metadata["page"] = i + 1  
    return documents


def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        add_start_index=True
    )

    chunks = text_splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):
        source = chunk.metadata.get("source", "Unknown")
        page = chunk.metadata.get("page", "?")
        chunk.metadata["paragraph"] = i + 1
        chunk.metadata["source"] = source
        chunk.metadata["page"] = page

    return chunks


def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

def build_faiss_index(file_paths, db_path="vectorstore/db_faiss"):
    all_documents = []
    for file_path in file_paths:
        documents = load_pdf(file_path)
        all_documents.extend(documents)
    text_chunk = create_chunks(all_documents)
    embedding_model = get_embedding_model()
    faiss_db = FAISS.from_documents(text_chunk, embedding_model)
    faiss_db.save_local(db_path)
    return faiss_db

def build_faiss_index_from_all_pdfs(db_path="vectorstore/db_faiss"):
    pdf_files = [os.path.join(path_directory, f) for f in os.listdir(path_directory) if f.lower().endswith('.pdf')]
    return build_faiss_index(pdf_files, db_path)

