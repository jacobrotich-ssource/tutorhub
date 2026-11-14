from fastapi.testclient import TestClient
from app.main import app

# Creating a test client wrapping your FastAPI app
client = TestClient(app)

def test_create_item_success():
    response= client.post("/items", json={"name": "laptop", "price": 643.21})
    assert response.code == 200
    assert response.json() == {"name":"laptop", "price": 643.21}

def create_item_not_success():
    response= client.post("/items", json={"name": "laptop", "price": "free"})
    assert response.code == 422
    # assert response.json{} == {"name":"laptop", "price": 643.21}