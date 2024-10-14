import logging
import os

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.home_page import HomePage
from utils.logging_conf import configure_logging
from utils.reporting import Reporting

# Configure logging settings
configure_logging()


def pytest_addoption(parser):
    """
    Adds a command-line option to select the browser.
    Usage: --browser=chrome or --browser=firefox
    """
    parser.addoption(
        "--browser", action="store", default="chrome", help="Type of browser: chrome or firefox"
    )


@pytest.fixture(scope="session")
def browser(request):
    """
    Fixture to initialize the browser session.
    It first attempts to install the WebDriver using webdriver_manager.
    If the installation fails, it falls back to using a local driver.
    """
    browser_choice = request.config.getoption("--browser")
    driver = None

    try:
        if browser_choice == "chrome":
            # Attempt to install ChromeDriver automatically via webdriver_manager
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            logging.info("ChromeDriver successfully installed using webdriver_manager.")
        elif browser_choice == "firefox":
            # Attempt to install GeckoDriver (Firefox) automatically via webdriver_manager
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            logging.info("GeckoDriver successfully installed using webdriver_manager.")
        else:
            raise ValueError(f"Unsupported browser: {browser_choice}")
    except WebDriverException as e:
        logging.error(f"Error installing the WebDriver with webdriver_manager: {e}")

        # Fallback to using local drivers if installation fails
        if browser_choice == "chrome":
            local_driver_path = os.path.join(os.getcwd(), 'drivers', 'chromedriver')
            logging.info(f"Using local ChromeDriver from: {local_driver_path}")
            driver = webdriver.Chrome(service=ChromeService(local_driver_path))
        elif browser_choice == "firefox":
            local_driver_path = os.path.join(os.getcwd(), 'drivers', 'geckodriver')
            logging.info(f"Using local GeckoDriver from: {local_driver_path}")
            driver = webdriver.Firefox(service=FirefoxService(local_driver_path))

    if driver is None:
        raise Exception(f"Error starting the browser: {browser_choice}")

    yield driver
    driver.quit()



@pytest.fixture
def home_page(browser):
    return HomePage(browser)

@pytest.fixture
def reporting(browser):
    return Reporting(browser)





