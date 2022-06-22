from selenium.webdriver.common.by import By
from HW15.page_objects.inventory_page import InventoryPage
from HW15.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    __user_name_input = (By.XPATH, '//*[@data-test="username"]')
    __password_input = (By.XPATH, '//*[@data-test="password"]')
    __login_button = (By.XPATH, '//*[@data-test="login-button"]')
    __login_error_message = (By.XPATH, '//*[@data-test="error"]')

    def __init__(self, driver):
        super().__init__(driver)

    def set_user_name(self, user_name):
        self.send_keys(self.__user_name_input, user_name)
        return self

    def set_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return InventoryPage(self._driver)

    def login_error_message(self):
        return self.wait_until_element_located(self.__login_error_message).text
