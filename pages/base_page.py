import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    """Base class for page objects with common Selenium methods."""

    ATR_VALUE = "value"  # Constant attribute name for element value

    def __init__(self, driver):
        """Initialize the WebDriver instance and set up logging."""
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def navigate_to(self, url):
        """Navigate to a specified URL and wait until the page is fully loaded."""
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def maximize_window(self):
        """Maximize the browser window."""
        self.driver.maximize_window()

    def get_page_urlbase(self):
        """Get and log the current URL of the page."""
        GET_URL_BASE = self.driver.current_url
        self.logger.info(f"URL is: {GET_URL_BASE}")
        return GET_URL_BASE

    def find_object(self, locator):
        """Find an element and return True if found, otherwise return False."""
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element found: {locator}")
        except (TimeoutException, NoSuchElementException):
            self.logger.error(f"Error finding element: {locator}")
            return False
        return element

    def wait_for_element(self, locator, timeout=5, condition=EC.visibility_of_element_located):
        """Wait for an element to be present and visible according to a specified condition."""
        try:
            element = WebDriverWait(self.driver, timeout).until(condition(locator))
            self.logger.info(f"Element located: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout waiting for element: {locator}")
            return False
        return True

    def click(self, locator):
        """
        Click on an element after ensuring it is clickable.
        If an exception occurs, stop the execution by raising the exception.
        """
        try:
            element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
            if element.is_displayed() and element.is_enabled():
                try:
                    self.logger.info(f"Element clickable: {locator}")
                    element.click()
                    self.logger.info(f"Clicked on: {locator}")
                except Exception as e:
                    self.logger.error(f"Error clicking element: {locator}, Exception: {str(e)}")
                    raise e
            else:
                self.logger.error(f"Element not clickable or not found: {locator}")
                raise Exception(f"Element not clickable or not found: {locator}")
        except TimeoutException:
            self.logger.error(f"Error waiting for element to be clickable: {locator}")
            raise

        return True

    def type_text(self, locator, text):
        """
        Type text into an input field after clearing any existing content.
        """
        element = self.find_object(locator)
        if element:
            try:
                element.clear()
                self.logger.info(f"Text cleared for: {locator}")
                element.send_keys(text)
                writted_text = element.get_attribute(self.ATR_VALUE)
                self.logger.info(f"Text: {writted_text} typed into element {locator}")
            except Exception as e:
                self.logger.error(f"Error typing text into locator {locator}: {str(e)}")
        else:
            self.logger.error(f"Cannot find element to type text into: {locator}")

    def get_locator_attribute(self, locator, attribute):
        """Retrieve an attribute from an element located by a locator."""
        element = self.find_object(locator)
        if element:
            attribute_value = element.get_attribute(attribute)
            self.logger.info(f"Retrieved {attribute}: {attribute_value} for {locator}")
            return attribute_value
        else:
            self.logger.error(f"Cannot extract attribute. {locator} not found")
            return False

    def get_element_text(self, locator):
        """Retrieve the text content from an element."""
        element = self.find_object(locator)
        if element:
            element_text = element.text
            self.logger.info(f"Retrieved text: {element_text} for {locator}")
            return element_text
        else:
            self.logger.error(f"Cannot extract text. {locator} not found")
            return False

    def get_all_element_attributes(self, element):
        """Retrieve and log all common attributes of a given element."""
        attributes = {
            "id": element.get_attribute("id"),
            "class": element.get_attribute("class"),
            "name": element.get_attribute("name"),
            "value": element.get_attribute("value"),
            "href": element.get_attribute("href"),
            "src": element.get_attribute("src"),
            "title": element.get_attribute("title"),
            "placeholder": element.get_attribute("placeholder"),
            "type": element.get_attribute("type"),
            "disabled": element.get_attribute("disabled"),
        }
        self.logger.info(f"Attributes: {attributes}")

    def click_count_times(self, locator, count):
        """
        Click an element a specified number of times.
        """
        if count is None or count == "":
            self.logger.warning(f"For element: {locator}, passenger quantity is: {count}")
            return False
        try:
            count = int(count)
        except ValueError:
            return False

        element = self.find_object(locator)
        if not element:
            self.logger.error(f"Element not found: {locator}")
            return False

        self.logger.info(f"Starting to click {count} times on: {locator}")
        for _ in range(count):
            element.click()
