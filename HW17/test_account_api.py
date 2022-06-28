from http import HTTPStatus


def test_post_user(register):
    response = register
    print("\n"+response.text)       # delete!!!!!
    assert response.status_code == HTTPStatus.CREATED
