# Verify API behavior with invalid token.
# Ensure unauthorized access is blocked.

import requests
import yaml

with open("config/config.yaml") as file:
    config = yaml.safe_load(file)


def test_invalid_token_get_notes():

    headers = {
        "x-auth-token": "invalidtoken"
    }

    response = requests.get(
        f"{config['api_url']}/notes",
        headers=headers
    )

    assert response.status_code == 401