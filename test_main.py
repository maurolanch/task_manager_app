from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

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

from operations import read_task

def test_endpoint_modify_task():
    updated_fields = {"status":"Finished"}
    response =  client.put("/task/2", json=updated_fields)

    assert response.status_code == 200
    assert response.json() == {
        **TEST_TASKS[1],
        **updated_fields
    }

    response = client.put(
        "/test/3", json=updated_fields
    )

    assert response.status_code == 404


def test_endpoint_delete_task():
    response = client.delete("/task/2")
    assert response.status_code == 200

    expected_response = TEST_TASKS[1]
    del expected_response["id"]

    assert response.json() == expected_response
    assert read_task(2) is None