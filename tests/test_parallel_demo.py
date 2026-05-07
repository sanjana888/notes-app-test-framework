import time


def test_parallel_1(driver):

    driver.get("https://practice.expandtesting.com/notes/app/login")

    time.sleep(30)

    assert "Notes" in driver.title


def test_parallel_2(driver):

    driver.get("https://practice.expandtesting.com/notes/app/login")

    time.sleep(30)

    assert "Notes" in driver.title