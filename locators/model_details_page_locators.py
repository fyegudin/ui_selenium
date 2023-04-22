from selenium.webdriver.common.by import By


class ModelDetailsPageLocators:
    SUPPORTED_COMMANDS_BUTTON = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[1]"
                                           "/div[1]/div/div/div[4]/button")
    ADD_COMMAND_BUTTON = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/"
                                    "div[1]/div/div[2]/button")
    SEARCH = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div[1"
                        "]/div/div[1]/div/div/input")
    FOUND = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div[2]"
                       "/div[1]/div[2]/div/div/div[3]")
    SELECT_CHECK_BOX = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div[2]/"
                                  "div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/input")
    SUMMARY = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div[1]/div/"
                         "div[1]/div[2]/span[1]/div")
    URL = "https://partners.xyte.io/models/d887e920-c8f0-4f8b-bc2e-e9bb40b21ffe/commands?page=1"
