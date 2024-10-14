from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):
    """Page object model for the home page with flight search functionalities."""

    # URL and element locators
    URL = "https://www.iberia.com/"
    DARK_FILTER = (By.XPATH, "//*[@id=onetrust-consent-sdk]/div[1]")
    COOKIE_BTN = (By.ID, "onetrust-accept-btn-handler")
    ORIGIN_TXTBOX = (By.ID, "flight_origin1")
    DESTINY_TXTBOX_CLICK = (By.XPATH, "//label[contains(.,'Destino')]")
    DESTINY_TXTBOX_TYPE = (By.ID, "flight_destiny1")
    START_DATE_TXTBOX_CLICK = (By.XPATH, "//label[contains(.,'Fecha ida')]")
    START_DATE_TXTBOX_TYPE = (By.ID, "flight_round_date1")
    END_DATE_TXTBOX_CLICK = (By.XPATH, "//label[contains(.,'Fecha vuelta')]")
    END_DATE_TXTBOX_TYPE = (By.ID, "flight_return_date1")
    PASSENGERS = (By.ID, "flight_passengers1")
    ADULT_PLUS_BTN = (By.CSS_SELECTOR, ".ibe-people-counter__list-item:nth-child(2) .ibe-people-counter__buttons-more")
    ADULT_MINUS_BTN = (By.XPATH, "//div[@id='people-counter-1']/ul/li[2]/div[2]/button")
    ADULT_COUNT = (By.ID, "adult1")
    CHILD_PLUS_BTN = (By.XPATH, "//*[@id='people-counter-1']/ul/li[5]/div[2]/button[2]")
    CHILD_MINUS_BTN = (By.XPATH, "//li[contains(@class, 'fc-people-counter-children')]//button[@data-people-counter-button='less']")
    CHILD_COUNT = (By.ID, "infants1")
    BABY_PLUS_BTN = (By.XPATH, "//*[@id='people-counter-1']/ul/li[6]/div[2]/button[2]")
    BABY_MINUS_BTN = (By.XPATH, "//li[contains(@class, 'fc-people-counter-babies')]//button[@data-people-counter-button='less']")
    BABY_COUNT = (By.XPATH, "//span[@data-people-type='babies']")

    flight_data_dict = None

    def __init__(self, driver):
        """Initialize the HomePage class, inherit from BasePage."""
        self.flight_data_dict = None
        super().__init__(driver)

    def print_flight_data(self):
        """Log the flight data dictionary."""
        self.logger.info(self.flight_data_dict)

    def navigate_home(self):
        """Navigate to the home page and maximize the browser window."""
        self.navigate_to(self.URL)
        self.maximize_window()

    def wait_to_darkfilter(self):
        """Wait for the dark filter (cookie banner) to disappear."""
        self.logger.info("Checking DARK_FILTER visibility.")
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.DARK_FILTER))
            self.logger.info(f"Element {self.DARK_FILTER} is no longer visible or has been removed.")
        except TimeoutException:
            self.logger.error(f"Timeout: Element {self.DARK_FILTER} is still visible.")

    def check_active_url(self):
        """Verify if the current URL matches the home page URL."""
        return self.URL == self.get_page_urlbase()

    def enter_origin(self, origin):
        """Enter the origin location in the flight search form."""
        self.logger.info("Starting to enter flight origin.")
        self.click(self.ORIGIN_TXTBOX)
        self.type_text(self.ORIGIN_TXTBOX, origin)

    def enter_destiny(self, destiny):
        """Enter the destination location in the flight search form."""
        self.click(self.DESTINY_TXTBOX_CLICK)
        self.type_text(self.DESTINY_TXTBOX_TYPE, destiny)

    def enter_stardate(self, start_date):
        """Enter the start date for the flight search."""
        self.click(self.START_DATE_TXTBOX_CLICK)
        self.type_text(self.START_DATE_TXTBOX_TYPE, start_date)

    def enter_enddate(self, end_date):
        """Enter the end date for the flight search."""
        self.click(self.END_DATE_TXTBOX_CLICK)
        self.type_text(self.END_DATE_TXTBOX_TYPE, end_date)

    def enter_passengers(self, adult_number, child_number, baby_number):
        """Select the number of passengers for the flight search."""
        adult_number = int(adult_number) - 1  # Adjust adult count
        self.click(self.PASSENGERS)
        self.clear_passengers()
        self.click_count_times(self.ADULT_PLUS_BTN, adult_number)
        self.click_count_times(self.CHILD_PLUS_BTN, child_number)
        self.click_count_times(self.BABY_PLUS_BTN, baby_number)
        self.logger.info("Finished entering passenger information.")

    def clear_passengers(self):
        """Reset the passenger count to default (1 adult, 0 children, 0 babies)."""
        self.logger.info("Resetting passenger count.")
        
        # Get current counts
        adult_minus_count = int(self.get_element_text(self.ADULT_COUNT))
        child_minus_count = int(self.get_element_text(self.CHILD_COUNT))
        baby_minus_count = int(self.get_element_text(self.BABY_COUNT))

        # Decrease adult count (to minimum 1)
        for _ in range(adult_minus_count - 1):
            self.logger.info(f"Decreasing adult count {adult_minus_count - 1} times.")
            self.click(self.ADULT_MINUS_BTN)

        # Decrease child count
        for _ in range(child_minus_count):
            self.logger.info(f"Decreasing child count {child_minus_count} times.")
            self.click(self.CHILD_MINUS_BTN)

        # Decrease baby count
        for _ in range(baby_minus_count):
            self.logger.info(f"Decreasing baby count {baby_minus_count} times.")
            self.click(self.BABY_MINUS_BTN)
