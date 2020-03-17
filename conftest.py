import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    yield language
