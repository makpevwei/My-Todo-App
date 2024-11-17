import streamlit as st
import todos_cli

todos = todos_cli.read_from_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    todos_cli.write_to_todos(todos)


st.title("My Todo App")
st.subheader("This app is to increase your productivity.")
st.write("Click on the checkbox to remove a todo.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todos_cli.write_to_todos(todos)
        del st.session_state[todo]
        st.rerun()
        
    
st.text_input(label="Enter a todo:", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")



