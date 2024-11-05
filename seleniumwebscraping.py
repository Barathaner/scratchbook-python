from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_text_with_selenium(url):
    # Setup Chrome WebDriver with user-agent and options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("start-maximized")

    # Pretend to be a normal user by setting a user-agent
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    # Create the WebDriver instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Navigate to the page
    driver.get(url)
    
    # Wait for the page to load completely (adjust as needed)
    time.sleep(5)  # Increase this time if the page is slow

    # Extract text from the body tag
    text = driver.find_element(By.TAG_NAME, "body").text
    
    # Close the driver
    driver.quit()
    
    return text

# Example usage
url = "https://www.bayer.com/media/aktuelle-studienergebnisse-bepanthenr-wund--und-heilsalbe-kann-mehr-als-klassische-wundbehandlung/"
print(scrape_text_with_selenium(url))
