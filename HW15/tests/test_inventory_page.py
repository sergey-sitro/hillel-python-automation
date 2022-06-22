import random


def test_inventory_items_a_to_z(login):
    inventory_page = login
    item_names = inventory_page.get_item_names()
    assert item_names == sorted(item_names)


def test_inventory_items_z_to_a(login):
    inventory_page = login
    inventory_page.change_sorting("Name (Z to A)")
    item_names = inventory_page.get_item_names()
    assert item_names == sorted(item_names)[::-1]


def test_inventory_items_price_low_to_high(login):
    inventory_page = login
    inventory_page.change_sorting("Price (low to high)")
    item_prices = inventory_page.get_item_prices_float()
    assert item_prices == sorted(item_prices)


def test_inventory_items_price_high_to_low(login):
    inventory_page = login
    inventory_page.change_sorting("Price (high to low)")
    item_prices = inventory_page.get_item_prices_float()
    assert item_prices == sorted(item_prices)[::-1]


def test_inventory_add_to_cart_badge(login):
    inventory_page = login
    item_added_to_cart = random.choice(inventory_page.get_add_to_cart_buttons())
    item_added_to_cart.click()
    badge = inventory_page.get_cart_badge()
    assert badge.text == "1"
