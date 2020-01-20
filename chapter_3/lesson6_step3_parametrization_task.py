import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
   # browser.quit()

URLS = [
    'https://stepik.org/lesson/236895/step/1'
]

@pytest.mark.parametrize('url', URLS)
def test_guest_should_see_login_link(browser, url):
    link = f"{url}"
    browser.get(link)

    #input = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(By.CSS_SELECTOR(".string-quiz__textarea")))
    time.sleep(10)
    input = browser.find_element_by_css_selector(".string-quiz__textarea")
    submit_button = browser.find_element_by_css_selector(".submit-submission")

    answer = math.log(int(time.time()))

    browser.implicitly_wait(15)
    input.send_keys(str(answer))
    submit_button.click()

    time.sleep(10)
    hint = browser.find_element_by_css_selector(".smart-hints__hint")
    assert hint.text == "Correct!", "The answer is wrong"
    print(hint.text)

