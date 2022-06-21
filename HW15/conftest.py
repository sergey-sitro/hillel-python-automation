import pytest
from HW15.utilities.driver_factory import DriverFactory
from HW15.page_objects.login_page import LoginPage


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_login_page(create_driver):
    return LoginPage(create_driver)

# @pytest.fixture
# def create_chrome_driver():
#     chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     chrome_driver.maximize_window()
#     yield chrome_driver
#     chrome_driver.quit()
#
#
# @pytest.fixture
# def chrome_login(create_chrome_driver):
#     username = 'standard_user'
#     password = 'secret_sauce'
#     create_chrome_driver.get(URL)
#     create_chrome_driver.maximize_window()
#     login_input_locator = '//*[@data-test="username"]'
#     login_input_element = create_chrome_driver.find_element(By.XPATH, login_input_locator)
#     password_input_locator = '//*[@data-test="password"]'
#     password_input_element = create_chrome_driver.find_element(By.XPATH, password_input_locator)
#     time.sleep(3)
#     login_input_element.send_keys(username)
#     password_input_element.send_keys(password)
#     time.sleep(3)
#     login_button_locator = '//*[@data-test="login-button"]'
#     login_button_element = create_chrome_driver.find_element(By.XPATH, login_button_locator)
#     login_button_element.click()
#     return create_chrome_driver
#
#
# @pytest.fixture
# def create_firefox_driver():
#     firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     firefox_driver.maximize_window()
#     yield firefox_driver
#     firefox_driver.quit()
#
#
# @pytest.fixture
# def firefox_login(create_firefox_driver):
#     username = 'standard_user'
#     password = 'secret_sauce'
#     create_firefox_driver.get(URL)
#     create_firefox_driver.maximize_window()
#     login_input_locator = '//*[@data-test="username"]'
#     login_input_element = create_firefox_driver.find_element(By.XPATH, login_input_locator)
#     password_input_locator = '//*[@data-test="password"]'
#     password_input_element = create_firefox_driver.find_element(By.XPATH, password_input_locator)
#     time.sleep(3)
#     login_input_element.send_keys(username)
#     password_input_element.send_keys(password)
#     time.sleep(3)
#     login_button_locator = '//*[@data-test="login-button"]'
#     login_button_element = create_firefox_driver.find_element(By.XPATH, login_button_locator)
#     login_button_element.click()
#     return create_firefox_driver
#
#
# @pytest.fixture
# def create_safari_driver():
#     safari_driver = webdriver.Safari()
#     safari_driver.maximize_window()
#     yield safari_driver
#     safari_driver.quit()
#
#
# @pytest.fixture
# def safari_login(create_safari_driver):
#     username = 'standard_user'
#     password = 'secret_sauce'
#     create_safari_driver.get(URL)
#     create_safari_driver.maximize_window()
#     login_input_locator = '//*[@data-test="username"]'
#     login_input_element = create_safari_driver.find_element(By.XPATH, login_input_locator)
#     password_input_locator = '//*[@data-test="password"]'
#     password_input_element = create_safari_driver.find_element(By.XPATH, password_input_locator)
#     time.sleep(3)
#     login_input_element.send_keys(username)
#     password_input_element.send_keys(password)
#     time.sleep(3)
#     login_button_locator = '//*[@data-test="login-button"]'
#     login_button_element = create_safari_driver.find_element(By.XPATH, login_button_locator)
#     login_button_element.click()
#     return create_safari_driver
