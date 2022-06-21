import time
from HW15.page_objects.inventory_page import InventoryPage


def test_login_success(get_login_page, get_inventory_page):
    login_page = get_login_page
    user_name = "standard_user"
    password = "secret_sauce"
    login_page.set_user_name(user_name)
    login_page.set_password(password)
    login_page.click_login_button()

    assert get_inventory_page.get_text == "Products"
    time.sleep(5)



# def test_login_chrome(chrome_login):
#     driver_chrome = chrome_login
#     title_element_text = driver_chrome.find_element(By.XPATH, "//*/span[@class='title']").text
#     assert title_element_text == "PRODUCTS", f"Unexpected title!\nActual: {title_element_text}\nExpected: PRODUCTS"
#     time.sleep(3)
#
#
# def test_login_firefox(firefox_login):
#     driver_firefox = firefox_login
#     title_element_text = driver_firefox.find_element(By.XPATH, "//*/span[@class='title']").text
#     assert title_element_text == "PRODUCTS", f"Unexpected title!\nActual: {title_element_text}\nExpected: PRODUCTS"
#     time.sleep(3)
#
#
# def test_login_safari(safari_login):
#     driver_safari = safari_login
#     title_element_text = driver_safari.find_element(By.XPATH, "//*/span[@class='title']").text
#     assert title_element_text == "Products", f"Unexpected title!\nActual: {title_element_text}\nExpected: Products"
#     time.sleep(3)
