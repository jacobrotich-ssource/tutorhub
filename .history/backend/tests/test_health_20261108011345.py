from fastapi.testclient import TestClient
from main import app

# Create a test client wrapping your FastAPI app
client = TestClient(app)