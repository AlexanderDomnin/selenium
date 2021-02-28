import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_names', action='store', default="chrome", help="Choose browser:chrome or firefox")
    parser.addoption('--language',action='store',default=None,help='Choose your language:ru,ent and etc..')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_names")
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart browser...")
        browser = webdriver.Chrome(options=options)
    elif (browser_name == "firefox"):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart browser...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser name should be chrome or firefox")
    yield browser
    print("\nquit browser...")
    browser.quit()
