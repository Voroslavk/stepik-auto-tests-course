from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")

@pytest.fixture
def browser(request):
    user_language = request.config.getoption("language")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    if user_language == 'ru':
        print("Чел из Рашки")
    elif user_language == 'en':
        print("Норм пацан")
    else:
        raise pytest.UsageError("--какая-то херовина")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    yield browser
    print("\nquit browser..")
    browser.quit()



