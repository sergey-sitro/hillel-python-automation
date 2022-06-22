import random


def test_inventory_items_a_to_z(login):
    """
        Decription: check that inventory items are ordered by name ascending by default

        Preconditions:
        - user is logged in
        - user is on "Inventory" page

        Steps:
        1. observe items order

        Expected result: items are ordered by name ascending by default
    """
    inventory_page = login
    item_names = inventory_page.get_item_names()
    assert item_names == sorted(item_names)


def test_inventory_items_z_to_a(login):
    """
        Decription: check that user can order inventory items by name descending

        Preconditions:
        - user is logged in
        - user is on "Inventory" page

        Steps:
        1. click on "filter" dropdown
        2. choose "Name (Z to A)" option
        3. observe items order

        Expected result: items are ordered by name descending
    """
    inventory_page = login
    inventory_page.change_sorting("Name (Z to A)")
    item_names = inventory_page.get_item_names()
    assert item_names == sorted(item_names)[::-1]


def test_inventory_items_price_low_to_high(login):
    """
        Decription: check that user can order inventory items by price ascending

        Preconditions:
        - user is logged in
        - user is on "Inventory" page

        Steps:
        1. click on "filter" dropdown
        2. choose "Price (low to high)" option
        3. observe items order

        Expected result: items are ordered by price ascending
    """
    inventory_page = login
    inventory_page.change_sorting("Price (low to high)")
    item_prices = inventory_page.get_item_prices_float()
    assert item_prices == sorted(item_prices)


def test_inventory_items_price_high_to_low(login):
    """
        Decription: check that user can order inventory items by price descending

        Preconditions:
        - user is logged in
        - user is on "Inventory" page

        Steps:
        1. click on "filter" dropdown
        2. choose "Price (high to low)" option
        3. observe items order

        Expected result: items are ordered by price descending
    """
    inventory_page = login
    inventory_page.change_sorting("Price (high to low)")
    item_prices = inventory_page.get_item_prices_float()
    assert item_prices == sorted(item_prices)[::-1]


def test_inventory_add_to_cart_badge(login):
    """
        Decription: check that cart badge counter appears upon adding item to cart

        Preconditions:
        - user is logged in
        - user is on "Inventory" page
        - user has no items in cart

        Steps:
        1. click on item's "Add To Cart" button
        2. observe cart badge counter

        Expected result:
        - cart badge counter appeared
        - cart badge counter has count of "1"
    """
    inventory_page = login
    item_added_to_cart = random.choice(inventory_page.get_add_to_cart_buttons())
    item_added_to_cart.click()
    badge = inventory_page.get_cart_badge()
    assert badge.text == "1"
