import pytest
from HW17.account_api import AccountApi
from random import randint


@pytest.fixture()
def register():
    req_username = "test_" + str(randint(1, 1000000000))
    body = {"userName": req_username, "password": "Qwerty1!"}
    response = AccountApi.post_user(AccountApi(), body=body)
    return response
