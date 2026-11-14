from fastapi.testclient import TestClient
from app.main import app

# Creating a test client wrapping your FastAPI app
client = TestClient(app)

def test_create_item_success():
    response= client.post("/items", json={"name": "laptop", "price": 643.21})
    assert response.status_code == 200
    assert response.json() == {"name":"laptop", "price": 643.21}

def test_create_item_not_success():
    response= client.post("/items", json={"name": "laptop", "price": "free"})
    assert response.status_code == 422
    # assert response.json{} == {"name":"laptop", "price": 643.21}