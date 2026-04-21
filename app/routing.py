def compute_confidence(scores):
    return 1 - sum(scores) / len(scores)

def should_escalate(confidence, threshold=0.5):
    return confidence < threshold
