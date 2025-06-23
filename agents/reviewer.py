# agents/reviewer.py

import os
import requests

SPUN_PATH = "data/chapter_1_spun.txt"
REVIEWED_PATH = "data/chapter_1_reviewed.txt"

OLLAMA_URL = "http://localhost:11434/api/generate"

def ollama_generate(prompt, model="llama3"):
    """
    Sends a prompt to the Ollama API and returns the model's response.
    """
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json()["response"]
    raise Exception(f"Ollama API error: {response.text}")

def review_chapter():
    """
    Refines the AI-spun chapter for clarity and style using Ollama.
    Saves the reviewed version to file.
    """
    if not os.path.exists(SPUN_PATH):
        print("Spun version not found. Please run the writer first.")
        return

    with open(SPUN_PATH, "r", encoding="utf-8") as f:
        spun_text = f.read()

    prompt = (
        "You are a professional editor. Improve the following book chapter "
        "for clarity, coherence, and flow. Ensure grammar and tone are consistent "
        "while preserving the creative style:\n\n"
        "--- BEGIN CHAPTER ---\n"
        f"{spun_text}\n"
        "--- END CHAPTER ---"
    )

    print("Reviewing chapter with Ollama...")
    reviewed_text = ollama_generate(prompt)

    with open(REVIEWED_PATH, "w", encoding="utf-8") as f:
        f.write(reviewed_text)

    print(f"Reviewed version saved to {REVIEWED_PATH}")

if __name__ == "__main__":
    review_chapter()
