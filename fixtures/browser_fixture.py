import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    chrome_options = Options()

    chrome_options.add_argument("--start-maximized")

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