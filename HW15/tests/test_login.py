import time
from selenium.webdriver.common.by import By


def test_login_chrome(chrome_login):
    driver_chrome = chrome_login
    title_element_text = driver_chrome.find_element(By.XPATH, "//*/span[@class='title']").text
    assert title_element_text == "PRODUCTS", f"Unexpected title!\nActual: {title_element_text}\nExpected: PRODUCTS"
    time.sleep(3)


def test_login_firefox(firefox_login):
    driver_firefox = firefox_login
    title_element_text = driver_firefox.find_element(By.XPATH, "//*/span[@class='title']").text
    assert title_element_text == "PRODUCTS", f"Unexpected title!\nActual: {title_element_text}\nExpected: PRODUCTS"
    time.sleep(3)


def test_login_safari(safari_login):
    driver_safari = safari_login
    title_element_text = driver_safari.find_element(By.XPATH, "//*/span[@class='title']").text
    assert title_element_text == "Products", f"Unexpected title!\nActual: {title_element_text}\nExpected: Products"
    time.sleep(3)
