import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

'''
Для фикстур можно задавать область покрытия фикстур. 
Допустимые значения: “function”, “class”, “module”, “session”. 
Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, 
один раз для модуля или один раз для всех тестов, запущенных в данной сессии. 
'''

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # All browsers will be closed at the end of the test suit
    #return browser

    # Browser will be closed at the end of each test
    yield browser
    browser.quit()

"""
параметр autouse=True, укажет, 
что фикстуру нужно запустить для каждого теста даже без явного вызова
"""
@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")