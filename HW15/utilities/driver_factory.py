from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    CHROME = 1
    FIRE_FOX = 2

    @staticmethod
    def create_driver(driver_id):
        if DriverFactory.CHROME == driver_id:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif DriverFactory.FIRE_FOX == driver_id:
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        else:
            driver = webdriver.Safari()

        return driver
