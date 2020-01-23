from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

"""
можно настраивать тестовые окружения с помощью передачи параметров через командную строку.

Это делается с помощью встроенной функции pytest_addoption и фикстуры request. Сначала добавляем в файле conftest обработчик опции в функции pytest_addoption, затем напишем фикстуру, которая будет обрабатывать переданные в опции данные. 

Давайте укажем параметр chrome:
pytest -s -v --browser_name=chrome chapter_3/lesson6_step6_send_params_thrugh_command_line/lesson6_step6_send_params_thrugh_command_line.py 

А теперь запустим тесты на Firefox:
pytest -s -v --browser_name=firefox chapter_3/lesson6_step6_send_params_thrugh_command_line/lesson6_step6_send_params_thrugh_command_line.py 

"""