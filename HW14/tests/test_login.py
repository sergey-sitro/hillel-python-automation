import time

from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'


def test_login_chrome(chrome_login, create_chrome_driver):

    driver_chrome = create_chrome_driver
    title_element_text = driver_chrome.find_element(By.XPATH, "//*/span[@class='title']").text
    assert title_element_text == "PRODUCTS", f"Unexpected title!\nActual: {title_element_text}\nExpected: PRODUCTS"
    time.sleep(3)


# def test_login_firefox(create_firefox_driver):
#     driver_firefox = create_firefox_driver
#     username = 'standard_user'
#     password = 'secret_sauce'
#     driver_firefox.get(URL)
#     driver_firefox.maximize_window()
#     login_input_locator = '//*[@data-test="username"]'
#     login_input_element = driver_firefox.find_element(By.XPATH, login_input_locator)
#     password_input_locator = '//*[@data-test="password"]'
#     password_input_element = driver_firefox.find_element(By.XPATH, password_input_locator)
#     time.sleep(3)
#     login_input_element.send_keys(username)
#     password_input_element.send_keys(password)
#     time.sleep(3)
#     login_button_locator = '//*[@data-test="login-button"]'
#     login_button_element = driver_firefox.find_element(By.XPATH, login_button_locator)
#     login_button_element.click()
#     title_element_text = driver_firefox.find_element(By.XPATH, "//*/span[@class='title']").text
#     assert title_element_text == "PRODUCTS", f"Unexpected title!\nActual: {title_element_text}\nExpected: PRODUCTS"
#     time.sleep(3)
#
#
# def test_login_safari(create_safari_driver):
#     driver_safari = create_safari_driver
#     username = 'standard_user'
#     password = 'secret_sauce'
#     driver_safari.get(URL)
#     driver_safari.maximize_window()
#     login_input_locator = '//*[@data-test="username"]'
#     login_input_element = driver_safari.find_element(By.XPATH, login_input_locator)
#     password_input_locator = '//*[@data-test="password"]'
#     password_input_element = driver_safari.find_element(By.XPATH, password_input_locator)
#     time.sleep(3)
#     login_input_element.send_keys(username)
#     password_input_element.send_keys(password)
#     time.sleep(3)
#     login_button_locator = '//*[@data-test="login-button"]'
#     login_button_element = driver_safari.find_element(By.XPATH, login_button_locator)
#     login_button_element.click()
#     title_element_text = driver_safari.find_element(By.XPATH, "//*/span[@class='title']").text
#     assert title_element_text == "Products", f"Unexpected title!\nActual: {title_element_text}\nExpected: Products"
#     time.sleep(3)
