# RAG Customer Support Assistant (LangGraph + Streamlit + Hugging Face)

A lightweight **Retrieval-Augmented Generation (RAG)** system that processes PDF documents and answers user queries using a graph-based workflow with optional Human-in-the-Loop (HITL) escalation.

---

## 🚀 Features

- 📄 PDF ingestion and chunking
- 🧠 Semantic search using embeddings (SentenceTransformers)
- 🗄️ Vector storage with ChromaDB
- 🤖 Lightweight LLM inference (Hugging Face `flan-t5`)
- 🔁 Graph-based orchestration using LangGraph
- ⚖️ Confidence-based routing & HITL escalation logic
- 💬 Streamlit UI for interaction

---

## 🏗️ System Flow

1. Upload PDF document  
2. Chunk + embed content  
3. Store embeddings in vector database (ChromaDB)  
4. User submits query  
5. LangGraph pipeline:
   - Retrieve relevant chunks
   - Generate answer using LLM
   - Compute confidence score
   - Decide whether to escalate or respond
6. Display response in Streamlit UI

---

## 🛠️ Tech Stack

- Streamlit (Frontend UI)
- LangGraph (Workflow orchestration)
- Hugging Face Transformers (LLM)
- SentenceTransformers (Embeddings)
- ChromaDB (Vector database)
- PyMuPDF (PDF parsing)

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

--- 

▶️ Run the App
```bash
streamlit run app.py
```

---

📁 Project Structure
```bash
rag-support-assistant/
│
├── app/               # UI + LangGraph workflow
├── core/              # LLM, embeddings, vector DB
├── ingestion/         # PDF loader + chunking pipeline
├── hitl/              # Escalation + storage logic
├── utils/             # Helpers
├── main.py            # Entry point
```

--- 
⚡ Notes
Designed for lightweight execution (CPU-friendly models)
Uses session state to maintain Streamlit stability
Built for educational + internship demonstration of RAG systems

---
🧠 Future Improvements
Multi-document support
Streaming responses
Feedback loop for retrieval improvement
Admin HITL dashboard
