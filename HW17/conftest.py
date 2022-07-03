import pytest
from HW17.account_api import AccountApi
from random import randint
from HW17.utilities.json_parser import json_parser
from HW17.config import test_password


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
