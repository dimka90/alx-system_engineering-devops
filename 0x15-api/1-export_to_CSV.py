#!/usr/bin/python3
"""This module a Rest Api that fetches information from the REST API"""
import csv
import requests
import sys
from sys import argv


def Userinfor(user_id):
    """
    Fetches user and todolist from REST API and extract some information
    Returns:
    - None: None
    """
    task = []
    count = 0
    completed_task = 0
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
        print(f"Error fetching TODOs for employee {user_id}: {e}")
        sys.exit(1)

    # getting username 
    for user in user_response_json:
        if user.get("id") == user_id:
            username = user.get("username")
    # Searching for the user with specific id in the todo list
    for todo in todo_response_json:
        # checking for the UserId in the todo list
        if todo.get("userId") == user_id:
            todo["username"] = username
            task.append(todo)
    print(task)

if __name__ == "__main__":
    user_id = int(argv[1])
    Userinfor(user_id)
