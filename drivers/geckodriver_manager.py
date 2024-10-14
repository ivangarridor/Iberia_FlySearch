import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def get_firefox_driver():
    """
    Initializes a Firefox WebDriver instance with a locally stored geckodriver.
    
    Uses a local geckodriver stored in the 'drivers' directory.
    
    Returns:
        WebDriver: A Firefox WebDriver instance.
    
    Raises:
        RuntimeError: If the WebDriver could not be initialized.
    """
    # Set the path to the geckodriver executable
    firefox_driver_path = os.path.join(os.getcwd(), 'drivers', 'geckodriver')

    if not os.path.exists(firefox_driver_path):
        raise RuntimeError(f"GeckoDriver not found at {firefox_driver_path}. Please download it manually.")

    # Configure Firefox options
    options = Options()
    options.add_argument("--headless") = True  # Run Firefox in headless mode (without UI)
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (useful for headless mode)
    options.add_argument("--no-sandbox")  # Disable the sandbox for Docker environments

    # Initialize the Firefox WebDriver using the local geckodriver path
    try:
        # Initialize the service with the path to geckodriver
        service = Service(executable_path=firefox_driver_path)
        driver = webdriver.Firefox(service=service, options=options)
    except Exception as e:
        raise RuntimeError(f"Failed to start Firefox WebDriver: {e}")

    return driver