from selenium.webdriver.common.by import By
from HW15.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    __email_input = (By.XPATH, '//*[@data-test="username"]')
    __password_input = (By.XPATH, '//*[@data-test="password"]')
    __login_button = (By.XPATH, '//*[@data-test="login-button"]')

    def __init__(self, driver):
        super().__init__(driver)

    def set_user_email(self, email):
        self.send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return self
