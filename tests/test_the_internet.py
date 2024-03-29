import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def visitPage(browser):
    browser.get("https://the-internet.herokuapp.com/")

def get_link_via_index(i,browser):
    return browser.find_elements(By.CSS_SELECTOR,"li a")[i].click()

def get_element_via_text(text,browser):
    return browser.find_element_by_xpath('//')


class TestTheInternet:

    # @pytest.mark.usefixtures("visitPage")
    # def test_abTest(self,browser):
    #     get_link_via_index(0,browser)
    #     # time.sleep(3)

    @pytest.mark.usefixtures("visitPage")
    def test_add_remove_element(self,browser):
        get_link_via_index(1,browser)
        # time.sleep(2)
        add_button = browser.find_element(By.CSS_SELECTOR, "#content button")
        del_button = browser.find_element(By.CSS_SELECTOR,"#example button")
        assert add_button is not None, "Button element with id 'goal' not found on the page"
        assert del_button is None, "Button element with id 'goal' not found on the page"
        add_button.click()

    