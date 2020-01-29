import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose language: en or ru")
    parser.addoption('--browser_name',
                     action='store',
                     default=None,
                     help='choose browser')

@pytest.fixture(scope="session")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        print("\nstart browser for test..")
    else:
        print(f"browser {browser_name} is not supperted in the test ")
        pytest.UsageError(f"--browser name should not be {browser_name}")
    yield browser
    print("\nquit browser..")
    browser.quit()