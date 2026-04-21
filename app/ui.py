import streamlit as st
import tempfile

from app.graph import build_graph
from ingestion.pipeline import ingest_pdf


st.title("RAG Customer Support Assistant")

graph = build_graph()


if "ingested" not in st.session_state:
    st.session_state.ingested = False

if "state" not in st.session_state:
    st.session_state.state = None



uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file and not st.session_state.ingested:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    ingest_pdf(tmp_path)

    st.session_state.ingested = True
    st.success("PDF processed successfully")



query = st.text_input("Ask a question")



if query and st.session_state.ingested:
    with st.spinner("Thinking..."):
        try:
            st.session_state.state = graph.invoke({"query": query})
        except Exception as e:
            st.error(f"Graph error: {e}")



state = st.session_state.state

if state is not None:
    st.write("### Answer")
    st.write(state.get("answer", "No answer"))

    st.write("### Confidence")
    st.write(state.get("confidence", 0))

    st.write("### Escalated?")
    st.write(state.get("escalate", False))

    st.write("### Retrieved Context")
    for doc in state.get("retrieved_docs", []):
        st.write(doc)