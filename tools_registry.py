from tools import retrieve, web_search, get_memory
from llm import generate_llm

def memory_tool(query):
    name = get_memory(query)
    if name:
        return f"User name is {name}"
    return None

def rag_tool(query):
    result = retrieve(query)
    if result and "No matching" not in result[0]:
        return result[0]
    return None

def web_tool(query):
    result = web_search(query)
    if result:
        return result
    return None

def llm_tool(query):
    return generate_llm(query)