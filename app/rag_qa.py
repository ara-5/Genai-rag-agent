import pickle
import faiss
from sentence_transformers import SentenceTransformer
from gpt4all import GPT4All

# Load documents
with open("ingestion/documents.pkl", "rb") as f:
    documents = pickle.load(f)

# Load FAISS index
index = faiss.read_index("ingestion/faiss_index.pkl")

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load ONE GPT4All model (FREE & offline)
llm = GPT4All(
    "orca-mini-3b-gguf2-q4_0.gguf",
    model_path="models"
)


print("✅ RAG system ready. Type a question or 'exit'.")

while True:
    query = input("\nYou: ")
    if query.lower() == "exit":
        break

    query_embedding = embedder.encode([query])
    distances, indices = index.search(query_embedding, k=2)

    context = "\n".join([documents[i] for i in indices[0]])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.generate(prompt, max_tokens=200)
    print("\nAI:", response)
