import pytest

from HW15.page_objects.inventory_page import InventoryPage
from HW15.utilities.driver_factory import DriverFactory
from HW15.page_objects.login_page import LoginPage
from HW15.utilities.run_settings import ReadConfig
from HW15.api_collections.account_api import AccountApi
from random import randint
from HW15.utilities.json_parser import json_parser
from HW15.config import test_password


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


@pytest.fixture()
def register():
    req_username = "test_" + str(randint(1, 1000000000))
    body = {"userName": req_username, "password": test_password}
    response = AccountApi().post_user(json=body)
    return response


@pytest.fixture()
def register_empty():
    response = AccountApi().post_user()
    return response


@pytest.fixture()
def generate_token(register):
    response = AccountApi().post_generate_token(json={"userName": json_parser(register.text)["username"],
                                                      "password": test_password})
    return response


@pytest.fixture()
def is_authorized(register):
    response = AccountApi().post_authorized(json={"userName": json_parser(register.text)["username"],
                                                  "password": test_password})
    return response


@pytest.fixture()
def get_user(register, generate_token):
    response_register = register
    uuid = json_parser(response_register.text)["userID"]
    response_token = generate_token
    token = json_parser(response_token.text)["token"]

    response = AccountApi().get_user(uuid=uuid, headers={"Authorization": "Bearer " + token})
    return response


@pytest.fixture()
def get_invalid_user(generate_token):
    response_token = generate_token
    token = json_parser(response_token.text)["token"]

    response = AccountApi().get_user(uuid="test", headers={"Authorization": "Bearer " + token})
    return response


@pytest.fixture()
def delete_user_success(register, generate_token):
    response_register = register
    uuid = json_parser(response_register.text)["userID"]
    response_token = generate_token
    token = json_parser(response_token.text)["token"]

    response = AccountApi().delete_user(uuid=uuid, headers={"Authorization": "Bearer " + token})
    return response


@pytest.fixture()
def delete_user_invalid(register, generate_token):
    response_token = generate_token
    token = json_parser(response_token.text)["token"]

    response = AccountApi().delete_user(uuid="test", headers={"Authorization": "Bearer " + token})
    return response
