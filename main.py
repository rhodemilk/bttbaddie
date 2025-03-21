from fastapi import FastAPI
from tasky import Task
from task_service import *
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (You can replace with specific origins)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


#initializing 2 instances of class Task()
tasks = [Task(), Task()]

#get post put delete
# @app.get(insert address)
@app.get("/")
def named():
    return "Hello world"

@app.get("/get-tasks")
def get():
    return tasks

@app.post("/task")
def posting(new_task: Task):
    tasks.append(new_task)
    return "Post succesful"

#get one task a way to pass down our variable to a function
@app.get("/task/{t_ID}")
def fun(t_ID: int):
    for task in tasks:
        if task.id == t_ID:
            return task
    return "task not found"

@app.put("/update-task/{t_ID}")
def update(t_ID: int, new_task: Task):
    for task in tasks:
        if task.id== t_ID:
            task.description = new_task.description
            task.is_complete = new_task.is_complete
            return "updated task"
    return "Task not found"


@app.delete("/delete/{t_ID}")
def delete(t_ID: int):
    for i, task in enumerate(tasks):
        if task.id == t_ID:
            tasks.pop(i)
            return "task deleted"
    return "task not found"






# # Import FastAPI and Depends from fastapi
# # FastAPI is the main framework class, Depends is used for dependency injection
# from fastapi import FastAPI, Depends
# # Import CORSMiddleware for handling Cross-Origin Resource Sharing
# from fastapi.middleware.cors import CORSMiddleware

# # Import database setup functions from db_task_model module
# from db_task_model import create_db_and_tables, get_session
# # Import Task model from task_model module
# from task_model import Task
# # Import all functions from db_task_service module
# from db_task_service import *  # Importing all database service functions

# # Import Session class from sqlmodel for type hinting
# from sqlmodel import Session


# # Create a FastAPI application instance
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins (You can replace with specific origins)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods
#     allow_headers=["*"],  # Allow all headers
# )


# # Startup event handler - executes when the application starts
# @app.on_event("startup")
# def on_startup():
#     # Create database tables if they don't exist
#     create_db_and_tables()

# # Root endpoint that returns a simple message
# @app.get("/")
# def root():
#     return "Hello World"

# # Endpoint to get all tasks
# @app.get("/tasks/all")
# def get_all(session: Session = Depends(get_session)):
#     # Use the get_session dependency to inject a database session
#     # Then call get_all_tasks service function with that session
#     return get_all_tasks(session)


# # Endpoint to create a new task
# @app.post("/task")
# def create(task: Task, session: Session = Depends(get_session)):
#     # Use the Task model for request body validation
#     # Inject database session and call create_task service function
#     return create_task(task, session)


# # Endpoint to update a task by ID
# @app.put("/{task_id}")
# def update(task_id: int, updated: Task, session: Session = Depends(get_session)):
#     # Get task_id from path parameter
#     # Get updated task data from request body
#     # Inject database session and call update_task service function
#     return update_task(task_id, updated, session)


# # Endpoint to delete a task by ID
# @app.delete("/task/delete/{task_id}")
# def delete(task_id: int, session: Session = Depends(get_session)):
#     # Get task_id from path parameter
#     # Inject database session and call delete_task service function
#     return delete_task(task_id, session)


# # Endpoint to get a specific task by ID
# @app.get("/get-task/{task_id}")
# def get(task_id: int, session: Session = Depends(get_session)):
#     # Get task_id from path parameter
#     # Inject database session and call get_task service function
#     return get_task(task_id, session)





