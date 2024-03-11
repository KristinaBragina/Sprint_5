from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver


class TestAuthentication(TestLocators):
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_authentication_by_button_login_in_main_page_success(self, driver):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.input_email_auth).send_keys('kristina_bragina_6_666@ya.ru')
        driver.find_element(*self.input_password_auth).send_keys('qwerty')
        driver.find_element(*self.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_make_the_order))
        assert expected_conditions.visibility_of_element_located(self.button_make_the_order)

    # Вход через кнопку «Личный кабинет»
    def test_authentication_by_button_personal_account_in_main_page_success(self, driver):
        driver.find_element(*self.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.input_email_auth).send_keys('kristina_bragina_6_666@ya.ru')
        driver.find_element(*self.input_password_auth).send_keys('qwerty')
        driver.find_element(*self.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_make_the_order))
        assert expected_conditions.visibility_of_element_located(self.button_make_the_order)

    # Вход через кнопку в форме регистрации
    def test_authentication_by_button_login_in_registration_form_success(self, driver):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_submit))
        driver.find_element(*self.button_login_in_registration_form).click()
        driver.find_element(*self.input_email_auth).send_keys('kristina_bragina_6_666@ya.ru')
        driver.find_element(*self.input_password_auth).send_keys('qwerty')
        driver.find_element(*self.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_make_the_order))
        assert expected_conditions.visibility_of_element_located(self.button_make_the_order)

    # Вход через кнопку в форме восстановления пароля
    def test_authentication_by_button_forgot_password_in_auth_form_success(self, driver):
        driver.find_element(*self.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_forgot_password).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            self.button_login_passwd_recovery_form))
        driver.find_element(*self.button_login_passwd_recovery_form).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.input_email_auth).send_keys('kristina_bragina_6_666@ya.ru')
        driver.find_element(*self.input_password_auth).send_keys('qwerty')
        driver.find_element(*self.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_make_the_order))
        assert expected_conditions.visibility_of_element_located(self.button_make_the_order)
