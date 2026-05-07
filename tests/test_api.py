import allure
from utils.api_client import login_api, get_notes, delete_note

@allure.title("Validate GET /notes API")
def test_get_notes_api():

    token = login_api()
    response = get_notes(token)

    allure.attach(
        response.text,
        name="GET Notes API Response",
        attachment_type=allure.attachment_type.JSON
    )

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 60
    ##assert response.elapsed.total_seconds() < 2
    assert "data" in response.json()


@allure.title("Validate DELETE /notes API")
def test_delete_note_api():

    token = login_api()
    get_response = get_notes(token)

    assert get_response.status_code == 200

    notes = get_response.json()["data"]

    if len(notes) == 0:
        assert True
        return

    note_id = notes[0]["id"]

    delete_response = delete_note(token, note_id)

    allure.attach(
        delete_response.text,
        name="DELETE Notes API Response",
        attachment_type=allure.attachment_type.JSON
    )

    assert delete_response.status_code in [200, 204]