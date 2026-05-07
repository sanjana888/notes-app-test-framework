import yaml
from pages.login_page import LoginPage

with open("config/config.yaml") as file:
    config = yaml.safe_load(file)


def test_invalid_login(driver):

    driver.get(config["base_url"])

    LoginPage(driver).login(
        "wrong@gmail.com",
        "wrongpassword"
    )

    assert "Notes React Application" in driver.title