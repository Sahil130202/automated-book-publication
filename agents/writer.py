# agents/writer.py

import os
import requests

RAW_PATH = "data/chapter_1_raw.txt"
SPUN_PATH = "data/chapter_1_spun.txt"

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

def spin_chapter():
    """
    Uses a local LLM to creatively rewrite the raw chapter.
    The rewritten version is saved for downstream processing.
    """
    if not os.path.exists(RAW_PATH):
        print("Raw chapter not found. Please run the scraper first.")
        return

    with open(RAW_PATH, "r", encoding="utf-8") as f:
        raw_text = f.read()

    prompt = (
        "You are a creative writer. Rewrite the following chapter in a more engaging, "
        "dramatic tone, using vivid descriptions and a storytelling style:\n\n"
        "--- BEGIN CHAPTER ---\n"
        f"{raw_text}\n"
        "--- END CHAPTER ---"
    )

    print("Spinning chapter with Ollama...")
    spun_text = ollama_generate(prompt)

    with open(SPUN_PATH, "w", encoding="utf-8") as f:
        f.write(spun_text)

    print(f"Spun version saved to {SPUN_PATH}")

if __name__ == "__main__":
    spin_chapter()
