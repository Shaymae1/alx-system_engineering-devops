#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    todo_url = url + "/user/{}/todos".format(argv[1])
    name_url = url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
