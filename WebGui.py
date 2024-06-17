import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("Web Todo")
st.subheader("If it helps then it helps!")
st.write("Enter a Todo below")

st.text_input(label="okay", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo',
              label_visibility='hidden')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

