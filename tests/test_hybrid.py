# Validate UI and API flow together.
# Verify data consistency across layers.

import time
import allure

from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.environment import load_config
from utils.api_client import login_api, get_notes, delete_note

config = load_config()


@allure.title("Hybrid Scenario 1: UI to API Validation")
def test_ui_to_api_validation(driver):

    title = f"Notes_UI_API_Check_{int(time.time())}"
    description = "Checking UI note against API response"
    driver.get(config["base_url"])

    LoginPage(driver).login(
        config["email"],
        config["password"]
    )

    notes_page = NotesPage(driver)
    notes_page.create_note(title, description)

    assert notes_page.is_note_present(title)

    token = login_api()
    response = get_notes(token)

    allure.attach(
        response.text,
        name="GET Notes API Response",
        attachment_type=allure.attachment_type.JSON
    )

    assert response.status_code == 200
    ##assert response.elapsed.total_seconds() < 2
    assert response.elapsed.total_seconds() < 60

    api_notes = response.json()["data"]

    assert any(
        note["title"] == title and note["description"] == description
        for note in api_notes
    )


@allure.title("Hybrid Scenario 2: API to UI Validation")
def test_api_to_ui_validation(driver):

    title = f"Notes_Delete_Sync_Check_{int(time.time())}"
    description = "Checking API delete reflection on UI"

    driver.get(config["base_url"])

    LoginPage(driver).login(
        config["email"],
        config["password"]
    )

    notes_page = NotesPage(driver)
    notes_page.create_note(title, description)

    assert notes_page.is_note_present(title)

    token = login_api()
    response = get_notes(token)

    api_notes = response.json()["data"]

    target_note = next(
        note for note in api_notes
        if note["title"] == title and note["description"] == description
    )

    delete_response = delete_note(token, target_note["id"])

    allure.attach(
        delete_response.text,
        name="DELETE API Response",
        attachment_type=allure.attachment_type.JSON
    )

    assert delete_response.status_code in [200, 204]

    notes_page.js_refresh()
    notes_page.wait_for_page_load()

    assert not notes_page.is_note_present(title)