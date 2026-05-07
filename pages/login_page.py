from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def login(self, email, password):

        email_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )

        password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        login_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )

        email_field.clear()
        email_field.send_keys(email)

        password_field.clear()
        password_field.send_keys(password)

        self.driver.execute_script("arguments[0].click();", login_button)