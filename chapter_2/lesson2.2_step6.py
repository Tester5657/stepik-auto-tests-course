from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # getting X
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    #
    radio1 = browser.find_element_by_css_selector('#peopleRule')
    people_checked = radio1.get_attribute('checked')
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    radio2 = browser.find_element_by_css_selector('[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio2)
    # radio2 = browser.find_element_by_css_selector('#robotsRule')
    radio2.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()