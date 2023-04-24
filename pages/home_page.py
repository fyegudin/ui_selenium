from .login_page import LoginPage
from ..locators.home_page_locators import HomePageLocators as HP


class HomePage(LoginPage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver.get(url)

    def click_models_button(self):
        models_button = self.element_is_visible(HP.MODELS_BUTTON)
        models_button.click()
        self.log_action("Clicked Models button")
