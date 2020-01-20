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

    input = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(By.CSS_SELECTOR(".quiz-component")))
    submit_button = browser.find_element_by_css_selector(".submit-submission")
    hint = browser.find_element_by_css_selector(".smart-hints__hint")

    answer = math.log(int(time.time()))

    browser.implicitly_wait(15)
    input.send_keys(answer)
    submit_button.click()

    assert hint.text == "Correct!", "The answer is wrong"
    print(hint.text)

