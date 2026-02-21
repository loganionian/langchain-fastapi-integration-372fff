import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_generate_text():
    response = client.post("/generate", json={"prompt": "Hello, world!"})
    assert response.status_code == 200
    assert "generated_text" in response.json()