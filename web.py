import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("by Jas Arora")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    todo_clean = todo.strip()  # Remove \n and spaces
    checkbox = st.checkbox(todo_clean, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
