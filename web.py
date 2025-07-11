import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip() + "\n"
    if todo != "\n":
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear input

# Create 2 columns side by side
left_col, right_col = st.columns([2, 1])  # Adjust the width ratio here

# LEFT COLUMN – Todo App
with left_col:
    st.title("My Todo App")
    st.subheader("by Jas Arora")
    st.write("This app is to increase your productivity.")

    remove_indexes = []

    for index, todo in enumerate(todos):
        todo_clean = todo.strip()
        checkbox = st.checkbox(todo_clean, key=f"todo_{index}")
        if checkbox:
            remove_indexes.append(index)

    if remove_indexes:
        for index in sorted(remove_indexes, reverse=True):
            todos.pop(index)
            del st.session_state[f"todo_{index}"]
        functions.write_todos(todos)
        st.rerun()

    st.text_input(label="", placeholder="Add a new todo...",
                  on_change=add_todo, key='new_todo')

# RIGHT COLUMN – Instructions
with right_col:
    st.header("📋 Instructions")
    st.set_page_config(layout="wide")
    st.markdown("""
  **How to use this app:**
    
    1.  If you want to add anything, 
		just write your task on the desired area.
    2.  If you want to edit any task, just write 
        your task on the desired area and press 
        the checkbox of the todo.
    3.  If you want to finish any task, you can 
        press the checkbox which is on the left 
        side of the task.
    ---
    **Tips to stay productive:**
    - Break big goals into smaller tasks.
    - Don’t overload — focus on 5-7 tasks/day.
    - Review your list every night.
    - Keep it simple and realistic.
    
    ---
    **Any Queries?**
    - Reach me out at: `imjasarora@gmail.com`
                """)
