import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

list_of_lessons = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

@pytest.mark.parametrize('lesson', list_of_lessons)
def test_parametrization(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)

    input = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".string-quiz__textarea")))
    submit_button = browser.find_element_by_css_selector(".submit-submission")

    answer = math.log(int(time.time()))
    input.send_keys(str(answer))
    submit_button.click()

    hint = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
    assert hint.text == "Correct!", "The answer is wrong"

    incorrect_hints = ''
    if hint.text != "Correct!":
        incorrect_hints += hint.text
    print(hint.text)

    try:
        assert 'Correct!' == hint.text
    except AssertionError:
        incorrect_hints += hint.text  # собираем ответ про Сов с каждой ошибкой