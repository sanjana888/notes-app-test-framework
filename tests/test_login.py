from pages.login_page import LoginPage
from config.environment import load_config
import time

config = load_config()

def test_login(driver):

    driver.get(config["base_url"])

    login_page = LoginPage(driver)

    login_page.login(
        config["email"],
        config["password"]
    )

    time.sleep(30)

    assert "notes" in driver.current_url.lower()