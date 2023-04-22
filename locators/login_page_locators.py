from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/div/div/form/div/button/div')
    URL = "https://partners.xyte.io/auth/sign-in"
