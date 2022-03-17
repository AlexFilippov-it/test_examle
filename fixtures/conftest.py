import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome') # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=800,600')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    s = Service('/Users/apple/Documents/test_examle/chromedriver')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.amazon.ca/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
