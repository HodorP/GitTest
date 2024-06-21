from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@allure.feature("Like a button")
@allure.story("Exist")
def test_like_a_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/like_a_button#")
    assert driver.find_element(By.CSS_SELECTOR, ".a-button")


@allure.feature("Like a button")
@allure.story("Click")
def test_like_a_button_click(driver):
    driver.get("https://www.qa-practice.com/elements/button/like_a_button#")
    assert driver.find_element(By.CSS_SELECTOR, ".a-button")
