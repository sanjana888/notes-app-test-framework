import allure
from utils.api_client import login_api, get_notes
from utils.performance_utils import measure_execution_time, log_performance
from config.environment import load_config

config = load_config()

@allure.title("API Performance Check - GET Notes")
def test_api_performance_get_notes():

    token = login_api()

    response, duration = measure_execution_time(
        lambda: get_notes(token)
    )

    log_performance("GET /notes response time", duration)

    allure.attach(
        str(duration),
        name="GET Notes Response Time",
        attachment_type=allure.attachment_type.TEXT
    )

    assert response.status_code == 200
    assert duration < 60


@allure.title("UI Performance Check - Page Load")
def test_ui_page_load_performance(driver):

    def load_page():

        driver.get(config["base_url"])

        import time
        time.sleep(5)

        return driver.execute_script(
            "return document.readyState"
        )

    state, duration = measure_execution_time(load_page)

    log_performance("UI page load time", duration)

    allure.attach(
        str(duration),
        name="UI Page Load Time",
        attachment_type=allure.attachment_type.TEXT
    )

    assert state == "complete"
  