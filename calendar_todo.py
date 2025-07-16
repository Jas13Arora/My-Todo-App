import streamlit as st
import functions
from datetime import date

st.set_page_config(layout="wide")
st.title("🗓️ Calendar-Based To-Do App with Notes")
st.caption("Made by Jas Arora")

# --- Date Picker ---
selected_date = st.date_input("Select a date", value=date.today())
selected_date_str = selected_date.strftime("%Y-%m-%d")

st.subheader(f"📝 To-Do for {selected_date_str}")

# --- Load Todos and Notes ---
todos = functions.get_todos_for_date(selected_date_str)
notes = functions.load_notes(selected_date_str)

# --- Layout Columns ---
left_col, right_col = st.columns([2, 1])

# --- LEFT SIDE ---
with left_col:
    remove_index = None

    for i, todo in enumerate(todos):
        todo_clean = todo.strip()
        key_prefix = f"{selected_date_str}_{i}"

        # Checkbox to mark task as done
        checkbox = st.checkbox(todo_clean, key=f"{key_prefix}_checkbox")
        if checkbox:
            remove_index = i
            break

        # Notes input for each task
        note_text = st.text_area(
            f"🗒️ Notes for: {todo_clean}",
            value=notes.get(todo_clean, ""),
            key=f"{key_prefix}_note",
            height=80
        )
        notes[todo_clean] = note_text
        functions.save_notes(selected_date_str, notes)

    # Remove task logic
    if remove_index is not None:
        removed_task = todos.pop(remove_index)
        removed_task_clean = removed_task.strip()
        if removed_task_clean in notes:
            del notes[removed_task_clean]
            functions.save_notes(selected_date_str, notes)
        functions.write_todos_for_date(todos, selected_date_str)
        del st.session_state[f"{selected_date_str}_{remove_index}_checkbox"]
        st.rerun()

    # Add new todo input
    def add_todo():
        todo = st.session_state["new_todo"].strip()
        if todo:
            todos.append(todo + "\n")
            functions.write_todos_for_date(todos, selected_date_str)
            st.session_state["new_todo"] = ""

    st.text_input("Add new to-do", placeholder="e.g., Finish homework", on_change=add_todo, key="new_todo")

# --- RIGHT SIDE ---
with right_col:
    st.header("📌 How to Use")
    st.markdown(f"""
- Select a date from the calendar.
- Add tasks using the input box.
- For each task, write explanation/notes below it.
- Notes are saved automatically.
- Tick a checkbox to remove the task and its note.

📩 Questions? [imjasarora@gmail.com](mailto:imjasarora@gmail.com)
""")
