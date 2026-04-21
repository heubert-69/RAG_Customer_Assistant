from sentence_transformers import SentenceTransformer
import streamlit as st


@st.cache_resource
def embed_texts(texts):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode(texts, convert_to_tensor=False)
