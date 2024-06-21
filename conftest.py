from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="session")
def driver(request):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver
