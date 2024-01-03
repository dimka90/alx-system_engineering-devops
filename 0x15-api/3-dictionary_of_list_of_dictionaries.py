#!/usr/bin/python3
"""This module a Rest Api that fetches information from the REST API"""
import json
import requests
import sys


def all_task():
    """
    Fetches user and todolist from REST API and extract some information
    Returns:
    - None: None
    """
    extracted_data_point = []
    user_data_url = "https://jsonplaceholder.typicode.com/users"
    todolist_data_url = "https://jsonplaceholder.typicode.com/todos"
    try:
        # sending a get request to the user url
        user_response = requests.get(user_data_url)
        # sending a get request to the todo list url
        todolist_respons = requests.get(todolist_data_url)
        # Raise Exception if anything gone bad
        user_response.raise_for_status() or todolist_respons.raise_for_status()
        # convert Response to Json objects
        user_response_json = user_response.json()
        # converting todolist to json objects
        todo_response_json = todolist_respons.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODOs for employee : {e}")
        sys.exit(1)

    # getting username
    data = {}
    for user in user_response_json:
        username = user.get("username")
    # Searching for the user with specific id in the todo list
    for todo in todo_response_json:
        # checking for the UserId in the todo list
        extracted_data = {"username": username,
                          "task": todo.get('title'),
                          "completed": todo.get('completed')}
        extracted_data_point.append(extracted_data)
        # creating a dictionary to store value
        data["{}".format(todo.get("userId"))] = extracted_data_point
    # filename
    filename = "todo_all_employees.json"
    # creating a dictionary to store value
    with open(filename, 'w') as file:
        # Write the extracted user data to the json file
        json.dump(data, file)


if __name__ == "__main__":
    all_task()
