from selenium.webdriver.common.by import By
from Utilities.Base import BaseClass


class LoginPage(BaseClass):
    email = (By.CSS_SELECTOR, "#ap_email")
    continue_button = (By.CSS_SELECTOR, "#continue[type=submit]")
    password = (By.CSS_SELECTOR, "#ap_password")
    sign_in_button = (By.CSS_SELECTOR, "#signInSubmit")

    def __init__(self, driver, wait, actions):
        super().__init__(driver, wait, actions)

    def login(self):
        self.sending_keys(LoginPage.email, "8466932669")

    def continue_click(self):
        self.click_if_visible(LoginPage.continue_button)

    def password_filed(self):
        self.sending_keys(LoginPage.password, "Sakesh@143")
        self.click_if_visible(LoginPage.sign_in_button)



