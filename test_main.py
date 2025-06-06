from main import app
from fastapi.testclient import TestClient

client = TestClient()

from conftest import TEST_TASKS

def test_endpoint_read_all_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == TEST_TASKS


def test_endpoint_get_task():
    response = client.get("/task/1")

    assert response.status_code == 200
    assert response.json() == TEST_TASKS[0]
    response = client.get("/task/5")

    assert response.status_code == 404


from operations import read_all_tasks

def test_endpoint_create_task():
    task = {
        "title":"To Define",
        "description": "will be done",
        "status":"Ready"
    }
    response = client.post("/task", json=task)

    assert response.status_code == 200
    assert response.json() == {**task, "id":3}
    assert len(read_all_tasks()) == 3

