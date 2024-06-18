from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome()
    return driver


def test_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
