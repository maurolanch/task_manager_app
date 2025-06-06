from main import app
from fastapi.testclient import TestClient

client = TestClient()

from conftest import TEST_TASKS

def test_endpoint_read_all_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == TEST_TASKS

