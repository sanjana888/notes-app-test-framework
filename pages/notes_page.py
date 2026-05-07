# Manage note creation actions.
# Validate saved notes in UI.

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NotesPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def create_note(self, title, description):

        time.sleep(5)

        self.driver.execute_script(
            "window.scrollTo(0, 0);"
        )

        add_btn = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@data-testid='add-new-note']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        time.sleep(2)

        title_input = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "title")
            )
        )

        title_input.clear()
        title_input.send_keys(title)

        description_input = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "description")
            )
        )

        description_input.clear()
        description_input.send_keys(description)

        create_btn = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[contains(text(),'Create')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            create_btn
        )

        time.sleep(5)

    def is_note_present(self, title):

        for _ in range(10):

            self.driver.refresh()

            time.sleep(3)

            if title in self.driver.page_source:
                return True

        return False

    def js_refresh(self):

        self.driver.execute_script(
            "location.reload();"
        )

        time.sleep(3)

    def wait_for_page_load(self):

        time.sleep(3)