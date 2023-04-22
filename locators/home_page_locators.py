from selenium.webdriver.common.by import By


class HomePageLocators:
    MODELS_BUTTON = (By.CSS_SELECTOR, "#root > div.page-wrapper.mantine-wq3d3d > div.open.mantine-yg7z42 > div > "
                                      "div:nth-child(2) > div.sidebar-nav > div:nth-child(2) > div:nth-child(2)"
                                      " > div > a")
    URL = "https://partners.xyte.io/"
