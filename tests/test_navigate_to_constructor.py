from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver, login


class TestNavigateToConstructor(TestLocators):
    # Проверка перехода из ЛК по клику на «Конструктор»
    def test_navigate_from_personal_account_to_constructor_by_header_success(self, driver, login):
        driver.find_element(*self.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.profile))
        driver.find_element(*self.header_of_page_constructor).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_make_the_order))
        assert expected_conditions.visibility_of_element_located(self.button_make_the_order)

    # Проверка перехода из ЛК по клику на лого
    def test_navigate_from_personal_account_to_constructor_by_logo_success(self, driver, login):
        driver.find_element(*self.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.profile))
        driver.find_element(*self.logo).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_make_the_order))
        assert expected_conditions.visibility_of_element_located(self.button_make_the_order)
