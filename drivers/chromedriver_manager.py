import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_chrome_driver():
    """
    Initializes a Chrome WebDriver instance with a locally stored chromedriver.
    
    Uses a local chromedriver stored in the 'drivers' directory.
    
    Returns:
        WebDriver: A Chrome WebDriver instance.
    
    Raises:
        RuntimeError: If the WebDriver could not be initialized.
    """
    # Set the path to the chromedriver executable
    chrome_driver_path = os.path.join(os.getcwd(), 'drivers', 'chromedriver')

    # Check if the chromedriver exists
    if not os.path.exists(chrome_driver_path):
        raise RuntimeError(f"ChromeDriver not found at {chrome_driver_path}. Please download it manually.")

    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")   # Run Chrome in headless mode (without UI)
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (useful for headless mode)
    options.add_argument("--no-sandbox")  # Disable the sandbox for Docker environments

    try:
        # Initialize the Chrome WebDriver using the local chromedriver path
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        raise RuntimeError(f"Failed to start Chrome WebDriver: {e}")

    return driver