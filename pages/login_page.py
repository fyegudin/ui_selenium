from ui_selenium.pages.base_page import BasePage
from ..locators.login_page_locators import LoginPageLocators as LP
from ui_selenium.data.test_data import Data as data


class LoginPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver.get(url)

    def _enter_username(self, username):
        username_field = self.element_is_visible(LP.USERNAME_FIELD)
        username_field.send_keys(username)
        self.log_action(f"Entered username: {username}")

    def _enter_password(self, password):
        password_field = self.element_is_visible(LP.PASSWORD_FIELD)
        password_field.send_keys(password)
        self.log_action("Entered password")

    def fill_the_field(self, locator, description):
        password_field = self.element_is_visible(locator)
        password_field.send_keys(description)
        self.log_action(f"Entered the follow {description}")

    def click_button(self, selector):
        login_button = self.element_is_visible(selector)
        login_button.click()
        self.log_action(f"Clicked {selector} button")

    def find_element(self, selector):
        self.element_is_visible(selector)

    def window_handels(self, driver):
        # get instance of first pop up  window
        whandle = driver.window_handles[1]
        # get instance of first pop up  window
        whandle = driver.window_handles[1]
        # switch to pop up window
        driver.switch_to.window(whandle)
        # get text of an element in pop window
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]").text
        return elem


    def login(self):
        self._enter_username(data.valid_username)
        self._enter_password(data.valid_password)
        self.click_button(LP.LOGIN_BUTTON)
