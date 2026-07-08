def route_question(question: str):

    question = question.lower()

    # ---------- Knowledge Questions ----------
    rag_keywords = [
        "what is",
        "explain",
        "define",
        "meaning",
        "how does",
        "how do",
    ]

    if any(keyword in question for keyword in rag_keywords):
        return "rag"

    # ---------- Fraud Investigation ----------
    fraud_keywords = [
        "fraud",
        "fraudulent",
        "suspicious",
        "aml",
        "money laundering",
        "high risk",
        "risk score",
        "unusual activity",
        "large transaction",
        "large transactions",
        "high value transaction",
        "high value transactions",
        "flagged transaction",
        "flagged transactions",
        "risky merchant",
        "risky merchants",
        "transaction monitoring",
        "anti money laundering",
    ]

    if any(keyword in question for keyword in fraud_keywords):
        return "fraud"

    return "sql"