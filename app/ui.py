import streamlit as st
import ollama

st.set_page_config(page_title="GenAI Local Chat", layout="centered")

st.title("🧠 Local GenAI Chat (Stable)")
st.write("This uses Ollama + Mistral running locally.")

question = st.text_input("Ask a question:")

if question:
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    st.subheader("🤖 Answer")
    st.write(response["message"]["content"])
