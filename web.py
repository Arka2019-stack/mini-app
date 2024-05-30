import streamlit as st
import functions

st.title("My Todo")
st.subheader("For improving the productivity")
st.text("This is a todo application")

todos = functions.read_todo()


def add_value():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()
        del st.session_state

st.text_input(label="write new todo", placeholder="write new todo here.....",
              key="new_todo", on_change=add_value)
