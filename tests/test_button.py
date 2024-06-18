from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def driver(request):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver


def test_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
