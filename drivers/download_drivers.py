import os
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Define the path where the drivers will be stored (assuming a "drivers" folder)
DRIVER_PATH = os.path.join(os.getcwd(), "drivers")

# Ensure the "drivers" folder exists, create it if not
if not os.path.exists(DRIVER_PATH):
    os.makedirs(DRIVER_PATH)

def download_chrome_driver():
    chrome_driver_path = ChromeDriverManager().install()
    print(f"ChromeDriver descargado en: {chrome_driver_path}")
    return chrome_driver_path

def download_gecko_driver():
    gecko_driver_path = GeckoDriverManager().install()
    print(f"GeckoDriver descargado en: {gecko_driver_path}")
    return gecko_driver_path

