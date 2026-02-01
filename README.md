# 🔐 GenAI RAG System – Local AI Document Q&A

A fully local **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about their documents using an open-source LLM — **no OpenAI API required**.

Built with:
- FAISS for vector search
- SentenceTransformers for embeddings
- GPT4All (Orca Mini) for local inference

---

## 🚀 Features
- 📄 Upload PDF documents
- 🧠 Semantic search using embeddings
- 🔍 Context-aware answers (RAG)
- 📴 Fully offline & privacy-preserving
- 💻 Runs on CPU (no GPU required)

---

## 🧱 Architecture

PDF → Chunking → Embeddings → FAISS
↓
User Query
↓
Retrieved Context
↓
Local LLM Response


---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/yourusername/genai-rag-agent
cd genai-rag-agent
pip install -r requirements.txt
python ingestion/load_documents.py
python app/rag_qa.py





🎯 Use Cases

Internal knowledge base

Resume / document analysis

Secure enterprise AI assistant

Legal / healthcare document QA