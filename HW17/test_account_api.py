import json
from http import HTTPStatus


def test_post_user(register):
    response = register
    req_username = json.loads(response.request.body)["userName"]
    assert response.status_code == HTTPStatus.CREATED
    assert json.loads(response.text)["userID"]
    assert req_username == json.loads(response.text)["username"]
    assert json.loads(response.text)["books"] == []
