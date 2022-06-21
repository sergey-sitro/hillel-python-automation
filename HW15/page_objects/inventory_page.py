from selenium.webdriver.common.by import By

from HW15.utilities.web_ui.base_page import BasePage


class InventoryPage(BasePage):
    _header = (By.XPATH, "//*/span[@class='title']")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def get_page_header(self):
        return self._header
