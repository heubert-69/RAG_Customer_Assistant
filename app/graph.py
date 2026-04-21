from langgraph.graph import StateGraph
from app.state import QueryState
from core.embeddings import embed_texts
from core.retriever import retrieve
from core.llm import generate_answer
from app.routing import compute_confidence, should_escalate
from hitl.escalation import escalate

def process_node(state):
    try:
        query = state["query"]

        query_emb = embed_texts([query])[0]
        docs, scores = retrieve(query_emb)

        state["retrieved_docs"] = docs

        context = "\n".join(docs[:2])

        state["answer"] = generate_answer(query, context)

        state["confidence"] = sum(scores) / len(scores)

        return state

    except Exception as e:
        state["answer"] = f"ERROR: {str(e)}"
        state["confidence"] = 0.0
        state["escalate"] = True
        return state
def decision_node(state):
    if should_escalate(state["confidence"]):
        return escalate(state["query"], state)
    return state

def build_graph():
    graph = StateGraph(QueryState)

    graph.add_node("process", process_node)
    graph.add_node("decision", decision_node)

    graph.set_entry_point("process")
    graph.add_edge("process", "decision")

    return graph.compile()
