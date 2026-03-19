from tools import (
    retrieve, web_search,
    add_memory, get_memory,
    quick_reflect
)
from llm import generate_llm
def detect_intent(query):
    q = query.lower()

    if "joke" in q:
        return "JOKE"

    if "my name" in q:
        return "MEMORY"

    if any(word in q for word in ["what", "who", "tell", "about"]):
        return "INFO"

    return "GENERAL"
def agentic_response(user_input, chat_history, show_reflection=True):
    query = user_input.strip()
    mem_status = add_memory(user_input)
    name = get_memory(query)
    intent = detect_intent(query)
    
    if "what is my name" in query.lower() and name:
        answer = f"Your name is {name}."
        source = "MEMORY"
    elif intent == "JOKE":
        answer = generate_llm("Tell a short funny joke.")
        if answer == "LLM Error":
            answer = "Why do programmers hate bugs? Because they bug them 😄"
            source = "FALLBACK"
        else:
            source = "LLM"

    elif intent == "INFO":
        rag = retrieve(query)

        if rag:
            answer = rag
            source = "RAG"
        else:
            web = web_search(query)

            if web:
                answer = web
                source = "WEB"
            else:
                answer = "Sorry, I couldn't find reliable info."
                source = "FAIL"

    
    else:
        answer = generate_llm(query)

        if answer == "LLM Error":
            answer = "I'm here to help! 😊"
            source = "FALLBACK"
        else:
            source = "LLM"
    # Memory  will acknowled
    if mem_status:
        answer = mem_status + "\n" + answer
    
    if show_reflection:
        answer += f"\n\n{quick_reflect(answer, source)} (Source: {source})"

    return answer