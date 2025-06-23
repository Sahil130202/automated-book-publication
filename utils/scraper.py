# utils/scraper.py

import os
from playwright.sync_api import sync_playwright

CHAPTER_URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
TEXT_PATH = "data/chapter_1_raw.txt"
SCREENSHOT_PATH = "data/screenshots/chapter_1.png"

def scrape_chapter():
    """
    Navigates to the target chapter URL, extracts the main text,
    and captures a full-page screenshot.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Navigating to: {CHAPTER_URL}")
        page.goto(CHAPTER_URL)

        # Extract main chapter content
        content = page.locator("div#mw-content-text").inner_text()
        os.makedirs(os.path.dirname(TEXT_PATH), exist_ok=True)
        with open(TEXT_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Text saved to {TEXT_PATH}")

        # Save a screenshot of the full page
        os.makedirs(os.path.dirname(SCREENSHOT_PATH), exist_ok=True)
        page.screenshot(path=SCREENSHOT_PATH, full_page=True)
        print(f"Screenshot saved to {SCREENSHOT_PATH}")

        browser.close()

if __name__ == "__main__":
    scrape_chapter()
