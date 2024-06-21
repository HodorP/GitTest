from selenium.webdriver.common.by import By
import allure


@allure.feature("Simple Button")
@allure.story("Exist")
def test_button_exist(driver):
    with allure.step("Open simple button page"):
        driver.get("https://www.qa-practice.com/elements/button/simple")
    with allure.step("Check button"):
        assert driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")


@allure.feature("Simple Button")
@allure.story("Click")
def test_button_click(driver):
    with allure.step("Open simple button page"):
        driver.get("https://www.qa-practice.com/elements/button/simple")
    with allure.step("Click button"):
        assert driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")


def test3():
    assert 1 == 2
