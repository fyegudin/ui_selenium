import os
import sys
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ui_selenium.utils.config_reader import ConfigReader
from ui_selenium.utils.webdriver_factory import WebDriverFactory


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click_element(self, locator):
        self.element_is_visible(locator).click()

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def send_keys_to_element(self, locator, keys):
        self.element_is_visible(locator).send_keys(keys)

    def take_screenshot(self, screenshot_name):
        self.driver.save_screenshot(f"sources/screenshots/{screenshot_name}.png")

    def log_action(self, action):
        with open(os.path.join(os.path.split(os.path.dirname(__file__))[0], 'logs', 'actions.log'), "a") as f:
            f.write(action + "\n")
