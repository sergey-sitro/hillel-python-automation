import pytest

from HW15.page_objects.inventory_page import InventoryPage
from HW15.utilities.driver_factory import DriverFactory
from HW15.page_objects.login_page import LoginPage
from HW15.utilities.run_settings import ReadConfig


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=int(ReadConfig.get_driver_id()))
    driver.get(ReadConfig.get_application_url())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def get_inventory_page(create_driver):
    return InventoryPage(create_driver)


@pytest.fixture()
def login(get_login_page):
    driver = get_login_page
    user_name = "standard_user"
    password = "secret_sauce"
    inventory_page = driver.set_user_name(user_name).set_password(password).click_login_button()
    return inventory_page
