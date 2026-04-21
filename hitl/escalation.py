from hitl.storage import save_escalation

def escalate(query, state):
    save_escalation(query)
    state["escalate"] = True
    state["answer"] = "Escalated to human support."
    return state
