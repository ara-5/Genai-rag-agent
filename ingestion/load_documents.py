from langchain_community.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os

# Folder containing PDFs
PDF_FOLDER = "data"

documents = []

for file in os.listdir(PDF_FOLDER):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(PDF_FOLDER, file))
        pages = loader.load()
        documents.extend([page.page_content for page in pages])

# Save documents
os.makedirs("ingestion", exist_ok=True)
with open("ingestion/documents.pkl", "wb") as f:
    pickle.dump(documents, f)

# Create embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(documents)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "ingestion/faiss_index.pkl")

print("✅ Documents ingested and index created")
