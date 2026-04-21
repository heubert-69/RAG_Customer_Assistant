from typing import List, Dict

class QueryState(dict):
    def __init__(self, query: str):
        super().__init__()
        self["query"] = query
        self["retrieved_docs"] = []
        self["answer"] = ""
        self["confidence"] = 0.0
        self["escalate"] = False


#A Class for an Answer Schema for The LLM
