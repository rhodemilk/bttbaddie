
from tasky import Task


#initializing 2 instances of class Task()
tasks = [Task(), Task()]

#get post put delete
# @app.get(insert address)

def name():
    return "Hello world"


def get():
    return tasks


def fun(new_task: Task):
    tasks.append(new_task)
    return "Post succesful"

#get one task a way to pass down our variable to a function

def fun(t_ID: int):
    for task in tasks:
        if task.id == t_ID:
            return task
    return "Task not found"


def update(t_ID: int, new_task: Task):
    for task in tasks:
        if task.id== t_ID:
            task.description = new_task.description
            task.is_complete = new_task.is_complete
            return "updated task"
    return "Task not found"



def delete(t_ID: int):
    for i, task in enumerate(tasks):
        if task.id == t_ID:
            tasks.pop(i)
            return "task deleted"
    return "Task not found"
