from selenium.webdriver.common.by import By
from utils.webActions import WebActions


class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    ERROR_MSG = (By.ID, "error")
    LOGIN_BUTTON = (By.ID, "submit")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='post-content']//p[@class='has-text-align-center']/strong")
    LOGIN_MESSAGE = (By.CSS_SELECTOR, ".post-title")

    def __init__(self, driver):
        self.driver = driver
        self.web_actions = WebActions(driver)

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.web_actions.enter_text(self.USERNAME_INPUT, username)
        self.web_actions.enter_text(self.PASSWORD_INPUT, password)
        self.web_actions.click(self.LOGIN_BUTTON)

