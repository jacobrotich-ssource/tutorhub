from fastapi.testclient import TestClient
from main import app

# Creating a test client wrapping your FastAPI app
client = TestClient(app)

def create_item_success():
    response= client.post("/itemss", json={"name": "laptop", "p"})