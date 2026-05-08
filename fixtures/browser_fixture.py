import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    chrome_options = Options()

    # Detect Jenkins environment
    is_jenkins = os.getenv("JENKINS_HOME")

    if is_jenkins:
        # Jenkins / CI execution
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        # Local execution
        chrome_options.add_argument("--start-maximized")

    # Selenium Grid check
    use_grid = os.getenv("GRID", "false").lower() == "true"

    if use_grid:

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=chrome_options
        )

    else:

        driver = webdriver.Chrome(
            options=chrome_options
        )

    yield driver

    driver.quit()