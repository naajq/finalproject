import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():
    def __init__(self, driver):
        self.driver = driver

    """ Method - Get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("\n\nCurrent url " + get_url)

    """ Method Screenshot"""

    def get_screenshot(self):
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + current_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\main_project\\screen\\' + name_screenshot)

    """ Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Get Value URL")
