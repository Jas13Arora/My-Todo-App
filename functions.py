import os
import json

TODO_FOLDER = "todos"
NOTES_FOLDER = "notes"

def get_todos_for_date(date_str):
    """Returns the list of todos for a specific date."""
    filepath = os.path.join(TODO_FOLDER, f"{date_str}.txt")
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as file:
        return file.readlines()

def write_todos_for_date(todos, date_str):
    """Writes todos to the specific date file."""
    os.makedirs(TODO_FOLDER, exist_ok=True)
    filepath = os.path.join(TODO_FOLDER, f"{date_str}.txt")
    with open(filepath, "w") as file:
        file.writelines(todos)

def load_notes(date_str):
    """Loads notes for a given date as a dictionary."""
    os.makedirs(NOTES_FOLDER, exist_ok=True)
    filepath = os.path.join(NOTES_FOLDER, f"{date_str}.json")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return {}

def save_notes(date_str, notes_dict):
    """Saves notes for a given date."""
    os.makedirs(NOTES_FOLDER, exist_ok=True)
    filepath = os.path.join(NOTES_FOLDER, f"{date_str}.json")
    with open(filepath, "w") as f:
        json.dump(notes_dict, f, indent=2)
