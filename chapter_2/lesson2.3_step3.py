import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)

    input = browser.find_element_by_css_selector('.form-control')
    input.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла