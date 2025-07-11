import streamlit as st
import functions

st.set_page_config(layout="wide")  # Moved this to the top

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip() + "\n"
    if todo != "\n":
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear input field

# Setup layout columns
left_col, right_col = st.columns([2, 1])

# --- LEFT SIDE: Main Todo App ---
with left_col:
    st.title("My Todo App")
    st.subheader("by Jas Arora")
    st.write("This app is to increase your productivity.")

    # ✅ Only remove the checked item AFTER the loop
    remove_index = None

    for index, todo in enumerate(todos):
        todo_clean = todo.strip()  # Remove \n and spaces
        checkbox = st.checkbox(todo_clean, key=f"todo_{index}")
        if checkbox:
            remove_index = index
            break  # Prevent multiple reruns during loop

    # ✅ Remove task outside the loop to avoid index shifting
    if remove_index is not None:
        todos.pop(remove_index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{remove_index}"]
        st.rerun()

    # Input to add new todo
    st.text_input(label="", placeholder="Add a new todo...",
                  on_change=add_todo, key='new_todo')

# --- RIGHT SIDE: Instructions ---
with right_col:
    st.header("📋 Instructions")
    st.markdown("""
**How to use this app:**

1. If you want to add anything, just write your task in the input box.
2. If you want to edit any task, write the updated task and press the checkbox of the old one.
3. If you want to finish any task, press the checkbox next to it.

---

**Tips to stay productive:**
- Break big goals into smaller tasks.
- Don’t overload — focus on 5-7 tasks/day.
- Review your list every night.
- Keep it simple and realistic.

---

**Any Queries?**
- Reach me at: `imjasarora@gmail.com`
""")
