import logging
from typing import Tuple, Any
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

Locator = Tuple[By, str]

class WebActions:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def click(self, by_locator: Locator) -> None:
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
            logging.info(f"Clicked on the element with {by_locator}")
        except NoSuchElementException:
            logging.error(f"Element with {by_locator} not found.")
            raise
        except TimeoutException:
            logging.error(f"Element with {by_locator} not clickable after 10 seconds.")
            raise

    def enter_text(self, by_locator: Locator, text: str) -> None:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered text in the element with {by_locator}")
        except NoSuchElementException:
            logging.error(f"Element with {by_locator} not found.")
            raise

    def get_element_text(self, by_locator: Locator) -> str:
        try:
            element_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
            logging.info(f"Text retrieved from element with {by_locator}: {element_text}")
            return element_text
        except NoSuchElementException:
            logging.error(f"Element with {by_locator} not found.")
            raise

    def navigate_to(self, url: str) -> None:
        try:
            self.driver.get(url)
            logging.info(f"Navigated to {url}")
        except Exception as e:
            logging.error(f"Error navigating to {url}: {e}")
            raise

    def scroll_to_element(self, by_locator: Locator) -> None:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logging.info(f"Scrolled to element with {by_locator}")
        except NoSuchElementException:
            logging.error(f"Element with {by_locator} not found.")
            raise

    def press_key(self, by_locator: Locator, key: Keys) -> None:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            element.send_keys(key)
            logging.info(f"Pressed {key} on element with {by_locator}")
        except NoSuchElementException:
            logging.error(f"Element with {by_locator} not found to send key.")
            raise

    def is_element_visible(self, by_locator: Locator) -> bool:
        """Checks if an element is visible on the page."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            logging.info(f"Element with {by_locator} is visible.")
            return True  # Explicitly return True to indicate visibility
        except TimeoutException:
            logging.error(f"Element with {by_locator} not visible within 10 seconds.")
            return False  # Return False to indicate non-visibility
        except NoSuchElementException:
            logging.error(f"Element with {by_locator} not found on the page.")
            return False  # Return False as the element is not present
