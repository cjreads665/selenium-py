import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

@pytest.fixture
def visitPage(browser):
    browser.get("https://the-internet.herokuapp.com/")

def get_elems_by_css(browser,selector):
    return browser.find_elements(By.CSS_SELECTOR,selector)

def get_link_via_index(browser,i):
    # return browser.find_elements(By.CSS_SELECTOR,"li a")[i].click()
    return get_elems_by_css(browser,'li a')[i].click()

def get_element_via_text(text,browser):
    return browser.find_element_by_xpath('//')


class TestTheInternet:

    @pytest.mark.usefixtures("visitPage")
    def test_abTest(self,browser):
        get_link_via_index(0,browser)
        # time.sleep(3)

    @pytest.mark.usefixtures("visitPage")
    def test_add_remove_element(self,browser):
        get_link_via_index(browser,1)
        btn_before_add = get_elems_by_css(browser,'#content button')
        assert len(btn_before_add) == 1, 'btn collection should be 1'
        btn_before_add[0].click()
        btn_after_add = get_elems_by_css(browser,'#content button')
        assert len(btn_after_add) > 1, 'btn collection should have 2 buttons after clicking on add'
        btn_after_add[1].click()
        assert len(btn_before_add) == 1, 'btn collection should be 1'


    @pytest.mark.usefixtures("visitPage")
    def test_basic_auth(self,browser):
        get_link_via_index(browser,2)
        # time.sleep(2)
        current_url = browser.current_url
        creds = "admin"
        url_with_creds = f"https://{creds}:{creds}@the-internet.herokuapp.com/basic_auth"
        browser.get(url_with_creds)
        # time.sleep(2)
        assert len(get_elems_by_css(browser,".example p")) >0, 'paragraph element is present after success login'

    @pytest.mark.usefixtures("visitPage")
    def test_for_broken_images(self,browser):
        get_link_via_index(browser,3)
        imgs = get_elems_by_css(browser,"img")
        print("fafdaadd")
        print(f"number : {len(imgs)}")
        print(222222)
        # get_elems_by_css(browser,"")


    