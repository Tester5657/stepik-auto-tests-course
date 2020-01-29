import pytest
from selenium import webdriver
import time

def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    time.sleep(4)

    """
    pytest -s -v --language=fr --browser_name=firefox chapter_3/lesson6_step8_parametrization/lesson6_step8_parametrization.py 

    """