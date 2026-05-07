import os
import pytest
import allure
from fixtures.browser_fixture import driver

# Capture screenshot when test fails.
# Save failure screenshot for reporting.

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        web_driver = item.funcargs.get("driver", None)

        if web_driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            web_driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )