from datetime import date, timedelta
import pytest
from HW15.utilities.json_parser import json_parser
from http import HTTPStatus


@pytest.mark.post_user
def test_post_user_response_status(register):
    """
    Description: Verify response status of successful registration

    Steps:
    1. Send POST https://www.saucedemo.com/Account/v1/User with payload:
    {"userName": <random_username>, "password": <test_password>}

    Expected result:
    - response code is 201
    - response reason is "Created"
    """

    response = register
    assert response.status_code == HTTPStatus.CREATED
    assert response.reason == "Created"


@pytest.mark.post_user
def test_post_user_response_body_new_user(register):
    """
    Description: Verify response body of new user

    Steps:
    1. Send POST https://www.saucedemo.com/Account/v1/User with payload:
    {"userName": <random_username>, "password": <test_password>}

    Expected result:
    - response body contains "userID"
    - response body contains "username" which is equal to request body "username"
    """

    response = register
    req_username = json_parser(response.request.body)["userName"]

    assert json_parser(response.text)["userID"]
    assert req_username == json_parser(response.text)["username"]
    assert json_parser(response.text)["books"] == []


@pytest.mark.post_user
def test_post_user_empty_status(register_empty):
    """
    Description: Verify response status and body while registering user with empty request body

    Steps:
    1. Send POST https://www.saucedemo.com/Account/v1/User with no payload

    Expected result:
    - response code is 400
    - response reason is "Bad Request"
    - response body contains "code" == "1200"
    - response body contains "message" == "UserName and Password required."
    """

    response = register_empty

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.reason == "Bad Request"
    assert json_parser(response.text)["code"] == "1200"
    assert json_parser(response.text)["message"] == "UserName and Password required."


@pytest.mark.post_generate_token
def test_post_generate_token(generate_token):
    """
    Description: Verify response of POST /GenerateToken request
    Steps:
    1. Register user with POST https://www.saucedemo.com/Account/v1/User requst
    2. Send POST https://www.saucedemo.com/Account/v1//GenerateToken with payload:
    {"userName": <registered_username>, "password": <test_password>}

    Expected result:
    - response code is 200
    - response reason is "OK"
    - response body contains "token"
    - response body contains "expires" which is equal to date of <today + 7 days>
    - response body contains "status" == "Success"
    - response body contains "result" == "User authorized successfully."
    """

    response = generate_token
    assert response.status_code == HTTPStatus.OK
    assert response.reason == "OK"
    assert json_parser(response.text)["token"]
    assert json_parser(response.text)["expires"].split("T")[0] == str(date.today() + timedelta(days=7))
    assert json_parser(response.text)["status"] == "Success"
    assert json_parser(response.text)["result"] == "User authorized successfully."


@pytest.mark.post_authorized
def test_registered_user_is_not_authorized(is_authorized):
    """
    Description: Verify that newly registered user is not authorized by default

    Steps:
    1. Send POST https://www.saucedemo.com/Account/v1/User with payload:
    {"userName": <random_username>, "password": <test_password>}
    2. Send POST https://www.saucedemo.com/Account/v1/Authorized with same payload
    Expected result:
    - response text is "false"
    """

    response = is_authorized
    assert response.text == "false"


@pytest.mark.get_user
def test_get_user(get_user):
    """
    Description: Verify response of Get /User request

    Steps:
    1. Send POST https://www.saucedemo.com/Account/v1/User with payload:
    {"userName": <random_username>, "password": <test_password>}
    2. Send POST https://www.saucedemo.com/Account/v1/Authorized with same payload
    3. Send GET https://www.saucedemo.com/Account/v1/User/<uuid_from_response_from_step_1> with header:
    {"Authorization": "Bearer + <token_from_step_2>"}

    Expected result:
    - response code is 200
    - response reason is "OK"
    - response body contains "userId"
    - response body contains "username"
    - response body contains "books" == []
    """

    response = get_user
    assert response.status_code == HTTPStatus.OK
    assert response.reason == "OK"
    assert json_parser(response.text)["userId"]
    assert json_parser(response.text)["username"]
    assert json_parser(response.text)["books"] == []


@pytest.mark.get_user
def test_get_invalid_user(get_invalid_user):
    """
        Description: Verify response of Get /User request for invalid userID

        Steps:
        1. Send POST https://www.saucedemo.com/Account/v1/User with payload:
        {"userName": <random_username>, "password": <test_password>}
        2. Send POST https://www.saucedemo.com/Account/v1/Authorized with same payload
        3. Send GET https://www.saucedemo.com/Account/v1/User/<random_invalid_userID> with header:
        {"Authorization": "Bearer + <token_from_step_2>"}

        Expected result:
        - response code is 401
        - response reason is "Unauthorized"
        - response body contains "code" == "1207"
        - response body contains "message" == "User not found!"
        """

    response = get_invalid_user
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.reason == "Unauthorized"
    assert json_parser(response.text)["code"] == "1207"
    assert json_parser(response.text)["message"] == "User not found!"


@pytest.mark.delete_user
def test_delete_user(delete_user_success):
    """
    Description: Verify response of successful DELETE /User request

    Steps:
    1. Send POST https://www.saucedemo.com/Account/v1/User with payload:
    {"userName": <random_username>, "password": <test_password>}
    2. Send POST https://www.saucedemo.com/Account/v1/Authorized with same payload
    3. Send DELETE https://www.saucedemo.com/Account/v1/User/<uuid_from_response_of_step_1> with header:
    {"Authorization": "Bearer + <token_from_step_2>"}

    Expected result:
    - response text is empty
    - response code is 204
    """

    response = delete_user_success
    assert response.text == ""
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.delete_user
def test_delete_user_invalid(delete_user_invalid):
    """
    Description: Verify response of DELETE /User request for invalid user

    Steps:
    1. Send POST https://www.saucedemo.com/Account/v1/User with payload:
    {"userName": <random_username>, "password": <test_password>}
    2. Send POST https://www.saucedemo.com/Account/v1/Authorized with same payload
    3. Send DELETE https://www.saucedemo.com/Account/v1/User/<random_invalid_userID> with header:
    {"Authorization": "Bearer + <token_from_step_2>"}

    Expected result:
    - response code is 200
    - response reason is "OK"
    - response contains "code" == "1207"
    - response contains "message" == "User Id not correct!"
    """

    response = delete_user_invalid
    assert response.status_code == HTTPStatus.OK
    assert response.reason == "OK"
    assert json_parser(response.text)["code"] == "1207"
    assert json_parser(response.text)["message"] == "User Id not correct!"
