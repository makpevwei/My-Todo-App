import time
import os

# Construct the path dynamically
file_path = os.path.join(os.path.dirname(__file__),'todos_file.txt')

# Get the current date and time in a human-readable format
NOW = time.strftime("%b %d, %Y %H:%M:%S")

# Default file path for storing todos
FILE_PATH = file_path


def read_from_todos(file_path=FILE_PATH):
    """
    Reads the list of todos from the specified file.

    Parameters:
        file_path (str): The path to the file storing todos. Defaults to FILE_PATH.

    Returns:
        list: A list of todos read from the file, where each todo is a string.
    """
    # Open the file in read mode and retrieve all todos
    with open(file_path, "r") as file:
        todos = file.readlines()
    return todos


def write_to_todos(todos_list, file_path=FILE_PATH):
    """
    Writes the provided list of todos to the specified file.

    Parameters:
        todos_list (list): The list of todos to write to the file.
        file_path (str): The path to the file storing todos. Defaults to FILE_PATH.
    """
    # Open the file in write mode and save the todos
    with open(file_path, "w") as file:
        file.writelines(todos_list)


def add_todos():
    """
    Adds a new todo item to the list.

    Prompts the user for a new todo, appends it to the list of todos,
    and saves the updated list to the file.
    """
    # Get the new todo from the user
    todo = input("Enter a todo: ").strip().capitalize() + "\n"
    # Read the current list of todos
    todos = read_from_todos()
    # Append the new todo
    todos.append(todo)
    # Write the updated list back to the file
    write_to_todos(todos)


def view_todos():
    """
    Displays the current list of todo items.

    Reads the todos from the file, removes newline characters for display,
    and prints each todo with its index.
    """
    # Read todos from the file
    todos = read_from_todos()
    # Clean todos by removing newline characters
    todos_cleaned = [todo.strip() for todo in todos]
    
    # Display each todo with its index
    for index, todo in enumerate(todos_cleaned, start=1):
        print(f"{index}: {todo}")


def edit_todos():
    """
    Edits an existing todo item.

    Prompts the user for the index of the todo to edit and the new text,
    then updates the todo and saves the changes back to the file.
    """
    try:
        # Get the index of the todo to edit
        number = int(input("Enter the number of the todo to edit: "))
        # Get the new todo text
        new_todo = input("Enter new todo: ").strip().capitalize() + "\n"
        # Read the current list of todos
        todos = read_from_todos()
        # Update the specified todo
        todos[number - 1] = new_todo
        # Write the updated list back to the file
        write_to_todos(todos)
        print("Todo updated successfully.")
    except (IndexError, ValueError) as error:
        # Handle invalid input or index out of range
        print(f"Error: {error}\nPlease enter a valid todo number.")


def delete_todos():
    """
    Deletes a specified todo item from the list.

    Prompts the user for the index of the todo to delete, removes it,
    and saves the updated list to the file.
    """
    try:
        # Get the index of the todo to delete
        number = int(input("Enter the number of the todo to delete: "))
        # Read the current list of todos
        todos = read_from_todos()
        # Remove the specified todo
        removed_todo = todos.pop(number - 1)
        # Write the updated list back to the file
        write_to_todos(todos)
        print(f"Todo '{removed_todo.strip()}' removed successfully.")
    except (IndexError, ValueError) as error:
        # Handle invalid input or index out of range
        print(f"Error: {error}\nPlease enter a valid todo number.")


def exit_app():
    """
    Exits the Todos application with a farewell message.
    """
    print("Exiting Todos App... Goodbye!")


def run_app():
    """
    Runs the main loop of the Todos application.

    Provides a menu for the user to choose from various actions
    and continuously prompts the user until they choose to exit.
    """
    # Display the current date and welcome message
    print(f"It is {NOW}")
    print("\nWelcome to Todos App")
    print("-" * 20)
    print("1. Add a todo")
    print("2. Show todos")
    print("3. Edit a todo")
    print("4. Delete a todo")
    print("5. Exit the application")
    
    # Infinite loop for the main menu
    while True:
        try:
            # Prompt the user for their choice
            choice = int(input("\nEnter your choice: "))
            # Match the choice with corresponding actions
            match choice:
                case 1:
                    add_todos()
                case 2:
                    view_todos()
                case 3:
                    edit_todos()
                case 4:
                    delete_todos()
                case 5:
                    exit_app()
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            # Handle invalid input (non-numeric)
            print("Error: Invalid input. Please enter a numeric choice.")


# Entry point of the program
if __name__ == "__main__":
    run_app()