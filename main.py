from fastapi import FastAPI, HTTPException
from models import (
    Task, 
    TaskWithID
)
from operations import (
    read_all_tasks,
    read_task,
    create_task,
    modify_task
)

app = FastAPI


@app.get("/tasks", response_class=list[TaskWithID])
def get_tasks():
    tasks = read_all_tasks()
    return tasks

