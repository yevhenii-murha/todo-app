import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()

    if not todo:
        st.warning("Please enter a non-empty todo.")
        return

    todo_to_add = todo + "\n"
    if todo_to_add in todos:
        st.warning("You’ve already added this todo.")
        return

    todos.append(todo_to_add)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    key = f"todo_{todo}".strip()
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[key]
        st.rerun()

st.text_input(label="Add new todo", placeholder="Type here...",
              on_change=add_todo, key="new_todo")
