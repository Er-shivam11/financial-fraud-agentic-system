def route_question(question: str):

    question = question.lower()

    rag_keywords = [
        "what is",
        "explain",
        "define",
        "meaning",
        "money laundering",
        "aml",
        "kyc",
        "fraud detection"
    ]

    for keyword in rag_keywords:
        if keyword in question:
            return "rag"

    return "sql"