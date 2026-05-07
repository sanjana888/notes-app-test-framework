from pages.login_page import LoginPage
from pages.notes_page import NotesPage
import yaml

with open("config/config.yaml") as file:
    config = yaml.safe_load(file)


def test_create_note_without_title(driver):

    driver.get(config["base_url"])

    LoginPage(driver).login(
        config["email"],
        config["password"]
    )

    notes_page = NotesPage(driver)

    notes_page.create_note(
        "",
        "Description without title"
    )

    assert "Add Note" in driver.page_source