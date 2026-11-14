from fastapi.testclient import TestClient
from main import app

# Creatin a test client wrapping your FastAPI app
client = TestClient(app)