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
            extracted_data = {"USER_ID": todo.get('userId'),
                              "USERNAME": username, "TASK_COMPLETED_STATUS":
                              todo.get('completed'),
                              "TASK_TITLE": todo.get("title")}
            extracted_data_point.append(extracted_data)
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    # filename
    filename = "{}.csv".format(user_id)

    # Open the CSV file in write mode

    with open(filename, 'w') as file:

        csv_writer = csv.DictWriter(file, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)

        # Write the extracted student data to the CSV file
        csv_writer.writerows(extracted_data_point)


if __name__ == "__main__":
    user_id = int(argv[1])
    Userinfor(user_id)
