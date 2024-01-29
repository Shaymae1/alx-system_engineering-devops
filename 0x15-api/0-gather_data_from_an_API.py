#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    
    employee_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employee_id))

    user = user_response.json()

    params = {"userid": employee_id}

    todos_response = requests.get(url + "todos", params=params)

    todos = todos_response.json()

    completed = []

    for todo todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(user.get("name").
        len(completed). len(todos)))
    for complete in completed:
        print("/t {}".format(complete))
