from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from HW15.utilities.web_ui.base_page import BasePage


class InventoryPage(BasePage):
    _header = (By.XPATH, "//*/span[@class='title']")
    _item_name = (By.XPATH, '//*[@class="inventory_item_name"]')
    _sorting_dropdown = (By.XPATH, '//*[@data-test="product_sort_container"]')
    _item_price = (By.XPATH, '//*[@class="inventory_item_price"]')
    _add_to_cart_buttons = (By.XPATH, '//*[@class="btn btn_primary btn_small btn_inventory"]')
    _cart_badge = (By.XPATH, '//*[@class="shopping_cart_badge"]')

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def get_page_header(self):
        return self.get_text(self._header)

    def get_item_names(self):
        return self.get_list_of_elements(self._item_name)

    def change_sorting(self, text):
        return Select(self.wait_until_element_located(self._sorting_dropdown)).select_by_visible_text(text)

    def get_item_prices(self):
        return self.get_list_of_elements(self._item_price)

    def get_item_prices_float(self):
        return [float(price.replace("$", "")) for price in self.get_item_prices()]

    def get_add_to_cart_buttons(self):
        return self.wait_until_all_elements_located(self._add_to_cart_buttons)

    def get_cart_badge(self):
        return self.wait_until_element_located(self._cart_badge)
