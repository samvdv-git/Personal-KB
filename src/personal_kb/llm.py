import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:8b"

def generate(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=60,
    )

    response.raise_for_status()

    return response.json()["response"]


def create_note(question: str) -> str:
    prompt = f"""
        Je bent een kennisassistent.

        Maak van onderstaande vraag een Obsidian note.

        Gebruik EXACT dit format:

        TITLE:
        ...

        SUMMARY:
        ...

        CONTENT:
        ...

        Vraag:

        {question}
        """

    return generate(prompt)