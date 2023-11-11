import os
import sys
from fastapi.testclient import TestClient

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from manager import app

client = TestClient(app)


def test_get_interactions():
    response = client.get("/interactions")
    assert response.status_code == 200


def test_create_interaction():
    interaction_data = {
        "settings": {
            "model_name": "GPT4",
            "role": "test",
            "prompt": "As a helpful IFS therapist chatbot..."
        }
    }
    response = client.post("/interactions", json=interaction_data)
    assert response.status_code == 201
    assert response.json()["settings"] == interaction_data["settings"]
