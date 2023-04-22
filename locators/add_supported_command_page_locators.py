from selenium.webdriver.common.by import By


class AddSupportedCommandPageLocators:
    FRIENDLY_NAME = (By.XPATH, "/html/body/div[23]/div/div/div[2]/div/div[2]/form/div/div/div[2]/div[1]/input")
    DESCRIPTION = (By.XPATH, "/html/body/div[23]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div[1]/input")
    NAME_SENT_TO_DEVICE = (By.XPATH, "/html/body/div[23]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div[1]/input")
    CREATE_BUTTON = (By.XPATH, "/html/body/div[23]/div/div/div[2]/div/div[2]/div[2]/button[2]/div/span")

    URL = "https://partners.xyte.io/models/d887e920-c8f0-4f8b-bc2e-e9bb40b21ffe/commands?page=1"
