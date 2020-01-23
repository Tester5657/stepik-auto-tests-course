import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")