#!/usr/bin/python3
"""This module a Rest Api that fetches information from the REST API"""
import requests
from sys import argv


def Userinfor(user_id):
    """
    Fetches user and todolist from REST API and extract some informatin
    
    Returns:
    - None: None
    """

    user_data = requests.get("https://jsonplaceholder.typicode.com/users")
    print(user_data.text)

    print(user_id)




if __name__ =="__main__":
    user_id = int(argv[1])
    Userinfor(user_id)
