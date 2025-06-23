# main.py

from utils.scraper import scrape_chapter
from agents.writer import spin_chapter
from agents.reviewer import review_chapter
from agents.human_editor import main as human_edit_main
from versioning.store import store_version_in_chromadb
from retrieval.rl_search import search_versions


def run_full_workflow():
    """
    Executes the full publication pipeline:
    scrape → spin → review → human edit → store.
    """
    print("\nStarting Automated Book Publication Workflow...\n")

    print("[1/4] Scraping content...")
    scrape_chapter()

    print("\n[2/4] Spinning chapter using AI Writer...")
    spin_chapter()

    print("\n[3/4] Reviewing chapter using AI Reviewer...")
    review_chapter()

    print("\n[4/4] Launching Human-in-the-Loop Editor...")
    human_edit_main()

    store_version_in_chromadb()

    print("\nWorkflow complete. Final chapter saved in data/chapter_1_final.txt")


if __name__ == "__main__":
    choice = input("Run (f)ull pipeline or (s)earch stored chapters? [f/s]: ").strip().lower()

    if choice == 'f':
        run_full_workflow()
    elif choice == 's':
        query = input("Enter search query: ")
        search_versions(query)
