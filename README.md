# 📄 GenAI RAG Document Assistant

**GenAI RAG** is a local AI-powered document assistant that allows you to **ask questions from your uploaded documents** using a **Retrieval-Augmented Generation (RAG)** system and **local GenAI models**.  
Built using **Python, Streamlit, GPT4All, FAISS, and Sentence-Transformers**.

---

## ⚡ Features

- Ask natural language questions about your documents.
- Uses a **local AI model** — no internet required after setup.
- Embeds documents using **SentenceTransformers**.
- Efficient **vector search with FAISS**.
- Simple **Streamlit UI** for easy interaction.
- Works offline — perfect for private, sensitive documents.

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend / UI | Streamlit |
| Language Model | GPT4All |
| Embeddings | Sentence-Transformers (`all-MiniLM-L6-v2`) |
| Vector Database | FAISS |
| Document Loader | LangChain Community (`PyPDFLoader`) |
| Python Version | 3.11 |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ara-5/Genai-rag-agent.git
cd Genai-rag-agent
