# Import necessary libraries
import streamlit as st  # Streamlit for creating the web application
import todos_cli  # Custom module for handling todos

# Read the existing todos from the file using the custom todos_cli module
todos = todos_cli.read_from_todos()

# Function to add a new todo item
def add_todo():
    # Get the new todo item from the input field and append it to the todos list
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    # Write the updated todos list back to the file
    todos_cli.write_to_todos(todos)

# Set the title of the Streamlit app
st.title("My Todo App")

# Add a subheader with HTML formatting for emphasis
st.subheader("This app is to increase your productivity")

# Display a brief description of the app's functionality
st.write("Click on the checkbox to remove a todo.")

# Loop through the list of todos and display each as a checkbox
for index, todo in enumerate(todos):
    # Assign a unique key by appending the index to the todo
    checkbox = st.checkbox(todo.strip(), key=f"{todo.strip()}_{index}")
    if checkbox:  # Check if the checkbox is selected
        todos.pop(index)  # Remove the selected todo from the list
        todos_cli.write_to_todos(todos)  # Save the updated todos list back to the file
        st.rerun()  # Reload the app to reflect changes

# Add a text input field for entering new todos
st.text_input(
    label="Enter a todo:",  # Label for the input field
    placeholder="Add a new todo...",  # Placeholder text in the input field
    on_change=add_todo,  # Trigger add_todo function when input changes
    key="new_todo"  # Key for accessing the input field's value in the session state
)