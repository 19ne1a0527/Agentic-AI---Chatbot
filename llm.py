import requests

def generate_llm(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            },
            timeout=10  #reduced timeout
        )
        return response.json().get("response", "").strip()
    except:
        return "LLM Error"