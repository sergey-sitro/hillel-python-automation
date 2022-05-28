import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="./geckodriver_linux_64_firefox")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://selenium-python.readthedocs.io/")
        elem = driver.find_element_by_xpath("//*[@id='searchbox']/div/form/input[1]")
        elem.send_keys("test")
        elem.send_keys(Keys.ENTER)
        sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/a[1]")
        elem.click()
        sleep(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()