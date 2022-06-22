def test_login_success(login):
    """
        Decription: check that user is able to log in successfully

        Steps:
        1. go to https://www.saucedemo.com/
        2. enter username = "standard_user"
        3. enter password = "secret_sauce"
        4. click "LOGIN" button

        Expected result:
        - "Inventory" page is opened
        - page header is "PRODUCTS"
        """
    inventory_page = login
    assert inventory_page.get_page_header == "PRODUCTS"


def test_login_fail_empty(get_login_page):
    """
        Decription: check that error message is shown upon clicking "LOGIN" button with empty credentials

        Steps:
        1. go to https://www.saucedemo.com/
        2. click "LOGIN" button

        Expected result:
        - Login error message is shown
        - Login error message is "Epic sadface: Username is required"
    """
    login_page = get_login_page
    login_page.click_login_button()
    assert login_page.login_error_message() == "Epic sadface: Username is required"


def test_login_fail_user_name_absent(get_login_page):
    """
        Decription: check that error message is shown upon clicking "LOGIN" button with empty username

        Steps:
        1. go to https://www.saucedemo.com/
        2. enter password = "secret_sauce"
        2. click "LOGIN" button

        Expected result:
        - Login error message is shown
        - Login error message is "Epic sadface: Username is required"
    """
    login_page = get_login_page
    password = "secret_sauce"
    login_page.set_password(password)
    login_page.click_login_button()
    assert login_page.login_error_message() == "Epic sadface: Username is required"


def test_login_fail_password_absent(get_login_page):
    """
        Decription: check that user is able to log in successfully

        Steps:
        1. go to https://www.saucedemo.com/
        2. enter username = "standard_user"
        3. click "LOGIN" button

        Expected result:
        - Login error message is shown
        - Login error message is "Epic sadface: Password is required"
    """
    login_page = get_login_page
    user_name = "standard_user"
    login_page.set_user_name(user_name)
    login_page.click_login_button()
    assert login_page.login_error_message() == "Epic sadface: Password is required"


def test_login_fail_invalid_credentials(get_login_page):
    """
        Decription: check that user is able to log in successfully

        Steps:
        1. go to https://www.saucedemo.com/
        2. enter username = "user"
        3. enter password = "password"
        3. click "LOGIN" button

        Expected result:
        - Login error message is shown
        - Login error message is "Epic sadface: Username and password do not match any user in this service"
    """
    login_page = get_login_page
    user_name = "user"
    password = "password"
    login_page.set_user_name(user_name)
    login_page.set_password(password)
    login_page.click_login_button()
    error_message = "Epic sadface: Username and password do not match any user in this service"
    assert login_page.login_error_message() == error_message
