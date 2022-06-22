import random


def test_inventory_items_a_to_z(get_login_page):
    login_page = get_login_page
    user_name = "standard_user"
    password = "secret_sauce"
    inventory_page = login_page.set_user_name(user_name).set_password(password).click_login_button()
    item_names = inventory_page.get_item_names()
    assert item_names == sorted(item_names)


def test_inventory_items_z_to_a(get_login_page):
    login_page = get_login_page
    user_name = "standard_user"
    password = "secret_sauce"
    inventory_page = login_page.set_user_name(user_name).set_password(password).click_login_button()
    inventory_page.change_sorting("Name (Z to A)")
    item_names = inventory_page.get_item_names()
    assert item_names == sorted(item_names)[::-1]


def test_inventory_items_price_low_to_high(get_login_page):
    login_page = get_login_page
    user_name = "standard_user"
    password = "secret_sauce"
    inventory_page = login_page.set_user_name(user_name).set_password(password).click_login_button()
    inventory_page.change_sorting("Price (low to high)")
    item_prices = inventory_page.get_item_prices_float()
    assert item_prices == sorted(item_prices)


def test_inventory_items_price_high_to_low(get_login_page):
    login_page = get_login_page
    user_name = "standard_user"
    password = "secret_sauce"
    inventory_page = login_page.set_user_name(user_name).set_password(password).click_login_button()
    inventory_page.change_sorting("Price (high to low)")
    item_prices = inventory_page.get_item_prices_float()
    assert item_prices == sorted(item_prices)[::-1]


def test_inventory_add_to_cart_badge(get_login_page):
    login_page = get_login_page
    user_name = "standard_user"
    password = "secret_sauce"
    inventory_page = login_page.set_user_name(user_name).set_password(password).click_login_button()
    item_added_to_cart = random.choice(inventory_page.get_add_to_cart_buttons())
    item_added_to_cart.click()
    badge = inventory_page.get_cart_badge()
    assert badge.text == "1"
