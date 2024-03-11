from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver, login


class TestLogout(TestLocators):
    # вход по кнопке «Войти в аккаунт» на главной
    def test_logout_of_personal_account_success(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_make_the_order))
        driver.find_element(*self.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.profile))
        driver.find_element(*self.button_logout).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_login))
        assert expected_conditions.visibility_of_element_located(self.button_login)
