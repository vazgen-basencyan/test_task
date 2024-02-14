from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver  # For type hinting
from selenium.webdriver.chrome.options import Options

def get_driver(browser_name: str) -> WebDriver:
    """
    Initializes and returns the WebDriver for the specified browser.

    Parameters:
    - browser_name (str): The name of the browser for which the WebDriver should be initialized.

    Returns:
    - WebDriver: The initialized WebDriver instance for the specified browser.

    Raises:
    - Exception: If the specified browser is not supported.
    """
    if browser_name.lower() == "chrome":
        options = Options()  # Correctly instantiate ChromeOptions
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    else:
        raise Exception(f"Browser not supported: {browser_name}")
