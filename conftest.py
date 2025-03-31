import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="ru",  # Значение по умолчанию, если параметр не указан
        help="Language for the test (e.g. 'ru' or 'en')"
    )

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
