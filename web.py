import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo+"\n")
    functions.write_file(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")

st.subheader("This is My To-Do app")
st.write("This app is to increase your productivity!!")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="ToDo", label_visibility='hidden', placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

