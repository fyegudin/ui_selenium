from ui_selenium.pages.base_page import BasePage
from .login_page import ActionOnPage
from ..locators.home_page_locators import HomePageLocators as HP


class HomePage(ActionOnPage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver.get(url)

    def click_models_button(self):
        models_button = self.element_is_visible(HP.MODELS_BUTTON)
        models_button.click()
        self.log_action("Clicked Models button")
