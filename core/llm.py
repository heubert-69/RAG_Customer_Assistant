from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        max_length=64
    )

def generate_answer(query, context):
    model = load_model()

    prompt = f"""
    Answer using context only.

    Context:
    {context}

    Question:
    {query}
    """

    out = model(prompt)
    return out[0]["generated_text"]
