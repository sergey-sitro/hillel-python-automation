import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture()
def create_chrome_driver():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def create_firefox_driver():
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture()
def create_safari_driver():
    safari_driver = webdriver.Safari()
    safari_driver.maximize_window()
    yield safari_driver
    safari_driver.quit()
