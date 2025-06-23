# versioning/store.py

import os
import json
import chromadb

FINAL_PATH = "data/chapter_1_final.txt"
METADATA_PATH = "data/chapter_1_metadata.json"

def store_version_in_chromadb():
    """
    Stores the final chapter and its metadata into a persistent ChromaDB collection.
    """
    if not os.path.exists(FINAL_PATH):
        print("Final chapter not found. Please run the editor first.")
        return

    with open(FINAL_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    # Use the new persistent Chroma client interface
    client = chromadb.PersistentClient(path="./chromadb_store")
    collection = client.get_or_create_collection("book_chapters")

    version_id = f"{metadata['editor']}_{metadata['edit_date']}"

    collection.add(
        documents=[content],
        ids=[version_id],
        metadatas=[metadata]
    )

    print(f"Version stored in ChromaDB with ID: {version_id}")
