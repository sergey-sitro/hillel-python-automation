import pytest

from HW15.page_objects.inventory_page import InventoryPage
from HW15.utilities.driver_factory import DriverFactory
from HW15.page_objects.login_page import LoginPage


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def get_inventory_page(create_driver):
    return InventoryPage(create_driver)
