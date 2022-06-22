from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def wait_until_element_located(self, locator):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait_until_element_located(locator)
        element.click()

    def get_text(self, locator):
        element = self.wait_until_element_located(locator)
        return element.text

    def send_keys(self, locator, value, is_clear=False):
        element = self.wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    @property
    def title(self):
        return self._driver.title

    def wait_until_all_elements_located(self, locator):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located(locator))

    def get_list_of_elements(self, locator):
        return [item.text for item in self.wait_until_all_elements_located(locator)]
