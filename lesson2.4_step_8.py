import math

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser: WebDriver = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # wait for $100
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    book_button = browser.find_element_by_id("book")
    book_button.click()

    # getting X and calculating y
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    
    # fill in answer
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()

finally:
    time.sleep(3)
    # browser.close()
