def plan(query):
    q = query.lower()

    if "my name" in q:
        return ["memory"]

    if "joke" in q:
        return ["llm"]

    if any(word in q for word in ["what", "who", "tell", "about"]):
        return ["rag", "web", "llm"]

    return ["llm"]