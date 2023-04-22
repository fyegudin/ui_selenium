from selenium.webdriver.common.by import By


class ModelsPageLocators:
    MODELS_BUTTON = (By.CSS_SELECTOR, "#cell-cell_0_model > div > div > a")
    URL = "https://partners.xyte.io/models?q%5Bs%5D=model+asc&page=1"
