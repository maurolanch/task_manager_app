import csv
from typing import Optional
from models import Task, TaskWithID

DATABASE_FILENAME = "tasks.csv"


colunn_fields = [
    "id", "title", "description", "status"
]

def read_all_tasks() -> list[TaskWithID]:
    with open(DATABASE_FILENAME) as csvfile:
        reader = csv.DictReader(
            csvfile
        )
        return [TaskWithID(**row) for row in reader]
    

