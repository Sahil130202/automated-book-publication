# retrieval/rl_search.py

import chromadb

# Initialize ChromaDB persistent client
client = chromadb.PersistentClient(path="./chromadb_store")

# Simple Q-table to track relevance feedback
q_table = {}

def search_versions(query, top_k=3):
    """
    Performs a semantic search for chapters matching the query.
    Collects relevance feedback and updates a Q-table.
    """
    collection = client.get_or_create_collection("book_chapters")

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    print(f"\nTop {top_k} results for: \"{query}\"\n")

    for i, (doc, metadata, id_) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0],
        results['ids'][0]
    )):
        print(f"\n--- RESULT {i + 1} ---")
        print(f"ID: {id_}")
        print(f"Editor: {metadata['editor']}")
        print(f"Date: {metadata['edit_date']}")
        print("Content (truncated):\n" + doc[:500])
        print("---")

        feedback = input("Was this result helpful? (y/n): ").strip().lower()
        reward = 1 if feedback == 'y' else 0
        q_table[id_] = q_table.get(id_, 0) + reward

    print("\nQ-table (Relevance Scores):")
    for id_, score in sorted(q_table.items(), key=lambda x: -x[1]):
        print(f"{id_}: {score}")
