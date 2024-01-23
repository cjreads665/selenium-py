from selenium import webdriver
import configparser

config = configparser.ConfigParser()

config.read('./config.ini')

base_url = config.get('General', 'BASE_URL', fallback='www.google.com')
# entering config for chromedriver

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

# Set the ChromeDriver executable path using the options parameter
chrome_options.add_argument("executable_path=chromedriver")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

url = base_url + '/'
# Rest of your Selenium code...
driver.get(url)

print(driver.title)

driver.quit()