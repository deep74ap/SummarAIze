
# 🧠 SummarAIze: Smart Assistant for Research Documents

**SummarAIze** is an AI-powered assistant that reads and reasons through your uploaded PDF or TXT documents. It delivers concise summaries, answers deep contextual questions, and challenges your understanding with logic-based evaluations. Designed for researchers, students, and professionals, SummarAIze bridges the gap between traditional summarizers and true comprehension — powered by **LangChain**, **FastAPI**, **Streamlit**, and **Groq API**.

---

## 🚀 Key Features

- 📄 **Document Upload**: Supports `.pdf` and `.txt` formats
- ✨ **Auto Summary**: Instantly generates a concise summary (≤ 150 words)
- 🤖 **Ask Anything Mode**: Natural language Q&A with grounded, source-based responses
- 🧠 **Challenge Me Mode**: Auto-generates logic-based questions and evaluates your answers
- 🔍 **Justified Answers**: Every response includes a citation or snippet from the document
- ⚡ **RAG Architecture**: Combines semantic search (FAISS) and fast inference (Groq API)
- 💡 **Bonus Capabilities**:
  - 🔁 Context memory for follow-up queries
  - 🎯 Highlighted text spans in answers for clarity

---
## 📁 Project Structure

```text
SummarAIze/
├── backend/
│   ├── main.py
│   ├── vector_database.py
│   └── rag_pipeline.py
├── frontend/
│   ├── streamlit_app.py
│   ├── summary.py
│   ├── ask_questions.py
│   └── self_eval.py
├── requirements.txt
└── .env
```
## 🧰 Tech Stack

| Technology       | Role                                             |
|------------------|--------------------------------------------------|
| **Streamlit**    | Web-based frontend UI                            |
| **FastAPI**      | Lightweight backend API server                   |
| **LangChain**    | Orchestration of retrieval and LLM prompting     |
| **Groq API**     | High-speed inference using Mixtral or LLaMA      |
| **PyMuPDF**      | PDF parsing and text extraction                  |
| **FAISS**        | Vector similarity search for document chunks     |

---




## 🏗️ Architecture Overview

```mermaid
graph TD
    A[User Uploads Document] --> B[Text Extraction (PyMuPDF)]
    B --> C[Chunking (LangChain Splitters)]
    C --> D[Embeddings + Indexing (FAISS)]
    D --> E[User Questions or Challenge Me Request]
    E --> F[Prompting via LangChain]
    F --> G[Response Generation via Groq API]
    G --> H[Answer with Justification & Highlighted Snippet]
```



## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/deep74ap/SummarAIze.git
cd summarAIze
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the Application

```bash
# Start FastAPI backend
uvicorn backend.main:app --reload

# Start Streamlit frontend (in separate terminal)
streamlit run frontend/streamlit_app.py
```

---

## 📽 Demo

> 🎥 Coming soon: A short YouTube walkthrough of SummarAIze in action.

---

## 🌟 What Makes SummarAIze Unique?

- ✅ Built specifically for long research and technical documents
- ✅ Uses RAG for accurate, reference-backed answers
- ✅ Provides comprehension-level challenge questions
- ✅ Fast response with Groq’s cutting-edge LLM support
- ✅ Modular architecture for easy customization and extension

---

## 🚧 Future Roadmap

- 📄 Support `.docx`, scanned OCR PDFs
- 🗣️ Voice input and multi-language summaries
- 💬 Conversation memory across sessions
- 📤 Export summaries and Q&A logs to PDF or Markdown

---

## 📝 Evaluation Alignment

| Criteria                          | Implementation Highlights                               |
|-----------------------------------|----------------------------------------------------------|
| ✔️ Accuracy + Justification       | Answers grounded in doc with citation                   |
| ✔️ Reasoning Mode                 | Auto Q&A + logic evaluation in "Challenge Me" mode      |
| ✔️ Clean UI/UX                    | Streamlit interface with minimal friction               |
| ✔️ Code Quality                   | Modular FastAPI + frontend/backend separation           |
| ✔️ Bonus Features                 | Memory + snippet highlighting support                   |
| ✔️ Contextual Awareness           | Uses FAISS and LangChain to maintain document context   |

## Screenshots
  **Landing Page**
  
  <img width="955" height="449" alt="Screenshot 1" src="https://github.com/user-attachments/assets/80214150-30d3-4f47-bf2c-220b7d5b202d" />
  
  **Document Summary Thinking**
  
<img width="959" height="444" alt="DocumentSummaryThinking" src="https://github.com/user-attachments/assets/ed58be73-c93b-4384-b1a0-41af7654f5a8" />

  **Summary**
  
<img width="914" height="444" alt="summaryofPDF" src="https://github.com/user-attachments/assets/1bcfcda7-f656-424c-bb73-175c9e14d338" />
  
  **Ask Question**
  
  <img width="959" height="455" alt="AskQuestion" src="https://github.com/user-attachments/assets/3f61e29e-dc9c-4de7-b8d9-727c1bb83ff8" />
  
  **Self Evaluation Quiz**
  
  <img width="959" height="452" alt="SelfEvalQues" src="https://github.com/user-attachments/assets/93292ddb-6a4a-4467-8983-5c89440ae4db" />

  
  **Evaluation of Quiz Reasoning**

  <img width="746" height="452" alt="EvaluationOFQuizwithReasoning" src="https://github.com/user-attachments/assets/12e202df-642e-4639-86e9-9cb70270b197" />
  
  **Self Evaluation Score**

<img width="953" height="452" alt="SelfEvalQUizans" src="https://github.com/user-attachments/assets/8aea9bc2-69f5-4c99-8696-c0426c0e3b32" />


**Deepak Chaurasiya**  
 Email: [deepak09012004@gmail.com](mailto:deepak09012004@gmail.com)  
GitHub: [deep74ap](https://github.com/deep74ap)
© 2025 — Smart Assistant Project
SummarAIze smarter. Learn deeper. 🚀
