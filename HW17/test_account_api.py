import json
from http import HTTPStatus


def test_post_user(register):
    response = register
    print("\n"+response.text)       # delete!!!!!
    req_username = response.request.body.split("&")[0].replace("userName=", "")
    print(req_username)
    assert response.status_code == HTTPStatus.CREATED
    assert json.loads(response.text)["userID"]
    assert req_username == json.loads(response.text)["username"]
    assert json.loads(response.text)["books"] == []
