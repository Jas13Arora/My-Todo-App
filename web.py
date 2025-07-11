import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip() + "\n"
    if todo != "\n":
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear input box

st.title("My Todo App")
st.subheader("by Jas Arora")
st.write("This app is to increase your productivity.")

# 🧠 Keep track of which todo to remove
remove_indexes = []

for index, todo in enumerate(todos):
    todo_clean = todo.strip()
    checkbox = st.checkbox(todo_clean, key=f"todo_{index}")
    if checkbox:
        remove_indexes.append(index)

# 💥 Remove checked todos after loop
if remove_indexes:
    for index in sorted(remove_indexes, reverse=True):
        todos.pop(index)
        del st.session_state[f"todo_{index}"]
    functions.write_todos(todos)
    st.rerun()

# ✍️ Input box
st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
