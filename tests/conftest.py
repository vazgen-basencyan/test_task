import pytest
from utils.webdriver_manager import get_driver

@pytest.fixture(scope="function")
def driver(request):
    # Get type from command line
    browser = request.config.getoption("--browser")
    # Use the  browser from comnd line
    driver = get_driver(browser)

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
