from selenium import webdriver
import configparser
from selenium.webdriver.common.by import By
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

# login forms 
url = base_url + '/testings'
driver.get(url) # get the title
driver.find_element(By.NAME,'fld_username').send_keys('abc123')
driver.implicitly_wait(20)

print(driver.title)

driver.quit()