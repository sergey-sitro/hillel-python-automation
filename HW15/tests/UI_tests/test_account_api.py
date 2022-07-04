from datetime import date, timedelta
import pytest
from HW15.utilities.json_parser import json_parser
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
    # Verify response while registering user with empty request body

    response = register_empty

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.reason == "Bad Request"
    assert json_parser(response.text)["code"] == "1200"
    assert json_parser(response.text)["message"] == "UserName and Password required."


@pytest.mark.post_generate_token
def test_post_generate_token(generate_token):
    response = generate_token
    assert response.status_code == HTTPStatus.OK
    assert response.reason == "OK"
    assert json_parser(response.text)["token"]
    assert json_parser(response.text)["expires"].split("T")[0] == str(date.today() + timedelta(days=7))
    assert json_parser(response.text)["status"] == "Success"
    assert json_parser(response.text)["result"] == "User authorized successfully."


@pytest.mark.post_authorized
def test_registered_user_is_not_authorized(is_authorized):
    # Verify that registered user is not authorized by default
    response = is_authorized
    assert response.text == "false"


@pytest.mark.get_user
def test_get_user(get_user):
    response = get_user
    assert response.status_code == HTTPStatus.OK
    assert response.reason == "OK"
    assert json_parser(response.text)["userId"]
    assert json_parser(response.text)["username"]
    assert json_parser(response.text)["books"] == []


@pytest.mark.get_user
def test_get_invalid_user(get_invalid_user):
    response = get_invalid_user
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.reason == "Unauthorized"
    assert json_parser(response.text)["code"] == "1207"
    assert json_parser(response.text)["message"] == "User not found!"


@pytest.mark.delete_user
def test_delete_user(delete_user_success):
    response = delete_user_success
    assert response.text == ""
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.delete_user
def test_delete_user_invalid(delete_user_invalid):
    response = delete_user_invalid
    assert response.status_code == HTTPStatus.OK
    assert response.reason == "OK"
    assert json_parser(response.text)["code"] == "1207"
    assert json_parser(response.text)["message"] == "User Id not correct!"
