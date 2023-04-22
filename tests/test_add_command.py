from ui_selenium.pages.login_page import ActionOnPage
from ui_selenium.data.test_data import Data as data
from ui_selenium.locators.home_page_locators import HomePageLocators as HP
from ..locators.models_page_locators import ModelsPageLocators as MP
from ..locators.model_details_page_locators import ModelDetailsPageLocators as MD
from ..locators.add_supported_command_page_locators import AddSupportedCommandPageLocators as ASC


class TestAddCommand:

    def test_create_new_command(self, driver):
        current_page = ActionOnPage(driver, data.login_url)
        current_page.login()
        # Navigate to Models > Super Turbo > Supported Commands
        current_page.click_button(HP.MODELS_BUTTON)
        current_page.click_button(MP.MODELS_BUTTON)
        current_page.click_button(MD.SUPPORTED_COMMANDS_BUTTON)
        # Add a new command
        current_page.click_button(MD.ADD_COMMAND_BUTTON)
        current_page.fill_the_field(ASC.FRIENDLY_NAME, data.friendly_name)
        current_page.fill_the_field(ASC.DESCRIPTION, data.description)
        current_page.fill_the_field(ASC.NAME_SENT_TO_DEVICE, data.name_sent_to_device)
        current_page.click_button(ASC.CREATE_BUTTON)
        # Verify that the command was created
        current_page.fill_the_field(MD.SEARCH, "cool")
        assert current_page.find_element(MD.FOUND) is None, "Model not created"
        current_page.take_screenshot("test_create_new_command_success")

    def test_create_duplication_command(self, driver):
        current_page = ActionOnPage(driver, data.login_url)
        current_page.login()
        # Navigate to Models > Super Turbo > Supported Commands
        current_page.click_button(HP.MODELS_BUTTON)
        current_page.click_button(MP.MODELS_BUTTON)
        current_page.click_button(MD.SUPPORTED_COMMANDS_BUTTON)
        # Add a new command
        current_page.click_button(MD.ADD_COMMAND_BUTTON)
        current_page.fill_the_field(ASC.FRIENDLY_NAME, data.friendly_name_failure)
        current_page.fill_the_field(ASC.DESCRIPTION, data.description)
        current_page.fill_the_field(ASC.NAME_SENT_TO_DEVICE, data.name_sent_to_device)
        current_page.click_button(ASC.CREATE_BUTTON)
        # Verify that the command creation failed
        actual_url = current_page.get_current_url()
        expected_url = MD.URL
        assert expected_url == actual_url, "Model duplicated"
        current_page.take_screenshot("test_create_duplicate_command_failure")
