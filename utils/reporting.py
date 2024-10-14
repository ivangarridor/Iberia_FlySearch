import os
import time
from pages.base_page import BasePage

# Logger setup (can be uncommented when implemented)
# logger = logging.getLogger(__name__)

class Reporting(BasePage):
    """
    Reporting class for handling screenshot functionality during tests.
    Inherits from BasePage to use WebDriver functionality.
    """

    def __init__(self, driver):
        """
        Initialize the Reporting class with the WebDriver.

        Args:
            driver (WebDriver): The WebDriver instance used for taking screenshots.
        """
        super().__init__(driver)

    def take_screenshot(self, name):
        """
        Takes a screenshot and saves it in the 'reports' directory with a timestamp.

        Args:
            name (str): The name of the screenshot file, typically related to the test.
        """
        # Get the current timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
    
        # Create the file name with timestamp
        file_name = f"{name}_{timestamp}.png"
        
        # Determine the project root directory
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Define the path for storing screenshots
        reports_folder = os.path.join(project_root, 'reports')
        
        # Log the reports folder path for reference
        self.logger.info(reports_folder)

        # Check if the 'reports' directory exists, and create it if not
        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder)
            self.logger.info(f"Created 'reports' directory at: {reports_folder}")
        else:
            self.logger.info(f"'reports' directory already exists at: {reports_folder}")
        
        # Generate the full file path for the screenshot
        file_path = os.path.join(reports_folder, file_name)
        
        # Take the screenshot and save it to the specified path
        self.driver.save_screenshot(file_path)

        # Log the screenshot save action
        self.logger.info("====================================================================================================")
        self.logger.info(f"{file_name} SCREENSHOT SAVED")
        self.logger.info("====================================================================================================")


    
        
    