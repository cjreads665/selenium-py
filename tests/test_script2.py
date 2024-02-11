import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # Setup
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

def test_search_google(browser):
    # Open Google
    browser.get("https://www.google.com")

    # Find the search box and enter a search query
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("apple" + Keys.RETURN)

    # Verify that the search results page is loaded
    assert "Google" in browser.title

    # Find all search result elements (using explicit wait for robustness)
    all_search_results = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
    )
    
    if all_search_results:
        # Verify that at least one search result contains "apple"
        assert any("apple" in result.text.lower() for result in all_search_results)
    else:
        # Handle the case where no search results are found
        print("No search results found containing 'apple'.")

if __name__ == "__main__":
    pytest.main()
