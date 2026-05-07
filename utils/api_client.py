import requests
from config.environment import load_config

config = load_config()
BASE_URL = config["api_url"]

def login_api():
    response = requests.post(
        f"{BASE_URL}/users/login",
        json={
            "email": config["email"],
            "password": config["password"]
        }
    )
    assert response.status_code == 200
    return response.json()["data"]["token"]

def get_notes(token):
    return requests.get(
        f"{BASE_URL}/notes",
        headers={"x-auth-token": token}
    )

def delete_note(token, note_id):
    return requests.delete(
        f"{BASE_URL}/notes/{note_id}",
        headers={"x-auth-token": token}
    )