import pytest

from HW17.utilities.json_parser import json_parser
from http import HTTPStatus


@pytest.mark.post_user
def test_post_user_response_status(register):
    # Verify response status of successful registration

    response = register

    assert response.status_code == HTTPStatus.CREATED
    assert response.reason == "Created"


@pytest.mark.post_user
def test_post_user_response_body_new_user(register):
    # Verify response body of new user

    response = register
    req_username = json_parser(response.request.body)["userName"]

    assert json_parser(response.text)["userID"]
    assert req_username == json_parser(response.text)["username"]
    assert json_parser(response.text)["books"] == []


@pytest.mark.post_user
def test_post_user_empty_status(register_empty):
    # Verify response status while registering user with empty request body

    response = register_empty

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.reason == "Bad Request"


@pytest.mark.post_user
def test_post_user_empty_response_body(register_empty):
    # Verify response body while registering user with empty request body

    response = register_empty

    assert json_parser(response.text)["code"] == "1200"
    assert json_parser(response.text)["message"] == "UserName and Password required."





