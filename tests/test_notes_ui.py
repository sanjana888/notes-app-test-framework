from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.environment import load_config

config = load_config()

def test_create_note(driver):

    title = "NotesApp_Create_Check"
    description = "Checking note creation from UI"

    driver.get(config["base_url"])

    LoginPage(driver).login(
        config["email"],
        config["password"]
    )

    notes_page = NotesPage(driver)

    notes_page.create_note(title, description)

    assert notes_page.is_note_present(title)