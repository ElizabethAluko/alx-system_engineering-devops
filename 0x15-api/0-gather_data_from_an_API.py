#!/usr/bin/python3
"""Display a given user todo list from REST API"""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    response_employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
    employee_data = response_employee.json()
    employee_name = employee_data['name']
    response_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
    todos_data = response_todos.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    print(f"Employee {employee_name} is done with tasks(
        {completed_tasks}/{total_tasks}): ")
    for todo in todos_data:
        if todo['completed']:
            print("\t", todo['title'])
