from fastapi import FastAPI
from tasky import Task

app = FastAPI()

#initializing 2 instances of class Task()
tasks = [Task(), Task()]

#post put delete get
# @app.get(insert address)
@app.get("/")
def name():
    return "Hello world"

@app.get("/get-tasks")
def get():
    return tasks





