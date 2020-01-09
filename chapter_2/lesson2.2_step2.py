from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    digit1 = browser.find_element_by_css_selector('#num1')
    digit2 = browser.find_element_by_css_selector('#num2')
    sumo = int(digit1.text) + int(digit2.text)


    select = Select(browser.find_element_by_css_selector("#dropdown"))
    # select.select_by_value("1")  # ищем элемент с текстом "Python"
    select.select_by_visible_text(str(sumo))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()