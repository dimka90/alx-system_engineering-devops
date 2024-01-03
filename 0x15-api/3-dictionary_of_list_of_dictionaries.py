#!/usr/bin/python3
"""This module fetches information from a REST API and exports
data in JSON format
"""
import json
import requests
import sys


def all_tasks():
    """
    Fetches user and todolist from REST API and extracts information
    Returns:
    - None: None
    """
    user_data_url = "https://jsonplaceholder.typicode.com/users"
    todolist_data_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        # Sending a get request to the user URL
        user_response = requests.get(user_data_url)
        # Sending a get request to the todo list URL
        todolist_response = requests.get(todolist_data_url)
        # Raise an exception if anything goes wrong
        user_response.raise_for_status()
        todolist_response.raise_for_status()
        # Convert responses to JSON objects
        user_response_json = user_response.json()
        todolist_response_json = todolist_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    # Organizing tasks data by user ID
    data = {}
    for user in user_response_json:
        user_id = user.get("id")
        username = user.get("username")
        data[str(user_id)] = []

        # Searching for tasks associated with the specific user ID
        for todo in todolist_response_json:
            if todo.get("userId") == user_id:
                task_info = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                }
                data[str(user_id)].append(task_info)

    # File name
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        # Write the organized data to the JSON file
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    all_tasks()
