def test_login_success(get_login_page):
    login_page = get_login_page
    user_name = "standard_user"
    password = "secret_sauce"
    inventory_page = login_page.set_user_name(user_name).set_password(password).click_login_button()
    assert inventory_page.get_page_header == "PRODUCTS"


def test_login_fail_empty(get_login_page):
    login_page = get_login_page
    login_page.click_login_button()
    assert login_page.login_error_message().text == "Epic sadface: Username is required"


def test_login_fail_user_name_absent(get_login_page):
    login_page = get_login_page
    password = "secret_sauce"
    login_page.set_password(password)
    login_page.click_login_button()
    assert login_page.login_error_message().text == "Epic sadface: Username is required"


def test_login_fail_password_absent(get_login_page):
    login_page = get_login_page
    user_name = "standard_user"
    login_page.set_user_name(user_name)
    login_page.click_login_button()
    assert login_page.login_error_message().text == "Epic sadface: Password is required"


def test_login_fail_invalid_credentials(get_login_page):
    login_page = get_login_page
    user_name = "user"
    password = "password"
    login_page.set_user_name(user_name)
    login_page.set_password(password)
    login_page.click_login_button()
    error_message = "Epic sadface: Username and password do not match any user in this service"
    assert login_page.login_error_message().text == error_message
