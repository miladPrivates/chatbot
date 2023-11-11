from fastapi.testclient import TestClient
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from manager import app

client = TestClient(app)


def test_get_messages():
    invalid_id = 'invalid_id'
    response = client.get(f"/interactions/{invalid_id}/messages")
    assert response.status_code == 404


def test_create_message():
    invalid_id = 'invalid_id'
    message_data = {
        "role": "human",
        "content": "Hello"
    }
    # invalid_id = '5ec08ec2-d28b-4dc5-b544-f2492fa2419e'
    response = client.post(f"/interactions/{invalid_id}/messages", json=message_data)
    assert response.status_code == 404
