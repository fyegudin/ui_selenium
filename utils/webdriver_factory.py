from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        if self.browser.lower() == "chrome":
            return webdriver.Chrome()
        elif self.browser.lower() == "firefox":
            return webdriver.Firefox()
        elif self.browser.lower() == "edge":
            return webdriver.Edge()
        else:
            raise Exception("Invalid browser name.")
