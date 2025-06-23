# agents/human_editor.py

import os
import datetime
import json

REVIEWED_PATH = "data/chapter_1_reviewed.txt"
FINAL_PATH = "data/chapter_1_final.txt"
METADATA_PATH = "data/chapter_1_metadata.json"

def edit_in_terminal(text):
    """
    Displays the reviewed chapter and prompts the user for edits.
    Returns either the original or the manually edited text.
    """
    print("\n================ REVIEWED CHAPTER ================\n")
    print(text)
    print("\n==================================================\n")

    choice = input("Would you like to edit this chapter? (y/n): ").strip().lower()
    if choice == 'y':
        print("\nEnter your edited version below (type 'END' on a new line to finish):\n")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        return "\n".join(lines)

    return text

def save_metadata(editor_name, notes):
    """
    Saves editor metadata, including name, timestamp, and optional notes.
    """
    metadata = {
        "editor": editor_name,
        "edit_date": datetime.datetime.now().isoformat(),
        "notes": notes
    }
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata saved to {METADATA_PATH}")

def main():
    if not os.path.exists(REVIEWED_PATH):
        print("Reviewed version not found. Please run the reviewer first.")
        return

    with open(REVIEWED_PATH, "r", encoding="utf-8") as f:
        reviewed_text = f.read()

    final_text = edit_in_terminal(reviewed_text)

    with open(FINAL_PATH, "w", encoding="utf-8") as f:
        f.write(final_text)
    print(f"Final version saved to {FINAL_PATH}")

    editor = input("Your name: ").strip()
    notes = input("Any notes for this version? (optional): ").strip()
    save_metadata(editor, notes)

if __name__ == "__main__":
    main()
