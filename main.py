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

@app.get("/task/{task_id}")
def get_task(task_id: int):
    task = read_task(task_id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task

@app.post("/task", response_class=TaskWithID)
def add_task(task: Task):
    return create_task(task)

