import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

URL = 'https://www.saucedemo.com/'


@pytest.fixture
def create_chrome_driver():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def chrome_login(create_chrome_driver):
    username = 'standard_user'
    password = 'secret_sauce'
    create_chrome_driver.get(URL)
    create_chrome_driver.maximize_window()
    login_input_locator = '//*[@data-test="username"]'
    login_input_element = create_chrome_driver.find_element(By.XPATH, login_input_locator)
    password_input_locator = '//*[@data-test="password"]'
    password_input_element = create_chrome_driver.find_element(By.XPATH, password_input_locator)
    time.sleep(3)
    login_input_element.send_keys(username)
    password_input_element.send_keys(password)
    time.sleep(3)
    login_button_locator = '//*[@data-test="login-button"]'
    login_button_element = create_chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    return create_chrome_driver


@pytest.fixture
def create_firefox_driver():
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture
def firefox_login(create_firefox_driver):
    username = 'standard_user'
    password = 'secret_sauce'
    create_firefox_driver.get(URL)
    create_firefox_driver.maximize_window()
    login_input_locator = '//*[@data-test="username"]'
    login_input_element = create_firefox_driver.find_element(By.XPATH, login_input_locator)
    password_input_locator = '//*[@data-test="password"]'
    password_input_element = create_firefox_driver.find_element(By.XPATH, password_input_locator)
    time.sleep(3)
    login_input_element.send_keys(username)
    password_input_element.send_keys(password)
    time.sleep(3)
    login_button_locator = '//*[@data-test="login-button"]'
    login_button_element = create_firefox_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    return create_firefox_driver


@pytest.fixture
def create_safari_driver():
    safari_driver = webdriver.Safari()
    safari_driver.maximize_window()
    yield safari_driver
    safari_driver.quit()


@pytest.fixture
def safari_login(create_safari_driver):
    username = 'standard_user'
    password = 'secret_sauce'
    create_safari_driver.get(URL)
    create_safari_driver.maximize_window()
    login_input_locator = '//*[@data-test="username"]'
    login_input_element = create_safari_driver.find_element(By.XPATH, login_input_locator)
    password_input_locator = '//*[@data-test="password"]'
    password_input_element = create_safari_driver.find_element(By.XPATH, password_input_locator)
    time.sleep(3)
    login_input_element.send_keys(username)
    password_input_element.send_keys(password)
    time.sleep(3)
    login_button_locator = '//*[@data-test="login-button"]'
    login_button_element = create_safari_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    return create_safari_driver
