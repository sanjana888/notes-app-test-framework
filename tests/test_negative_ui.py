import yaml

with open("config/config.yaml") as file:
    config = yaml.safe_load(file)


def test_invalid_page_access(driver):

    driver.get(
        config["base_url"] + "/invalidpage"
    )

    assert "Notes React Application" in driver.title