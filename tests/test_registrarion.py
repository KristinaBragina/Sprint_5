import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver, random_email, random_password, invalid_random_email


class TestRegistration(TestLocators):
    # Регистрация аккаунта пользователя с валидными значениями инпутов
    def test_registration_new_account_success_submit(self, driver, random_email, random_password):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_submit))
        driver.find_element(*self.input_name).send_keys('Kristina')
        driver.find_element(*self.input_email).send_keys(random_email)
        driver.find_element(*self.input_password).send_keys(random_password)
        driver.find_element(*self.button_submit).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_login))
        assert expected_conditions.visibility_of_element_located(self.button_register)

    # Регистрация аккаунта при пустом поле "Имя"
    def test_registration_name_is_empty_failed_submit(self, driver, random_email, random_password):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_submit))
        driver.find_element(*self.input_name).send_keys('')
        driver.find_element(*self.input_email).send_keys(random_email)
        driver.find_element(*self.input_password).send_keys(random_password)
        driver.find_element(*self.button_submit).click()
        assert expected_conditions.visibility_of_element_located(self.button_submit)

    # Регистрация аккаунта при вводе невалидного значения в поле Email — отсутствует @
    def test_registration_invalid_email_format_without_at_failed_submit(self, driver, invalid_random_email, random_password):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_submit))
        driver.find_element(*self.input_name).send_keys('Kristina')
        driver.find_element(*self.input_email).send_keys(f'{invalid_random_email}yandex.ru')
        driver.find_element(*self.input_password).send_keys(random_password)
        driver.find_element(*self.button_submit).click()
        assert expected_conditions.visibility_of_element_located(self.button_submit)

    # Регистрация аккаунта при вводе невалидного значения в поле Email — отсутствует домен первого уровня
    def test_registration_invalid_mail_format_with_invalid_domain_failed_submit(self, driver, invalid_random_email, random_password):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_submit))
        driver.find_element(*self.input_name).send_keys('Kristina')
        driver.find_element(*self.input_email).send_keys(f'{invalid_random_email}@ya.')
        driver.find_element(*self.input_password).send_keys(random_password)
        driver.find_element(*self.button_submit).click()
        assert expected_conditions.visibility_of_element_located(self.button_submit)

    # Регистрация аккаунта при вводе валидного по длине значения в поле "Пароль"
    @pytest.mark.parametrize('valid_password', ['123456', '1234567', '123456789012'])
    def test_registration_valid_length_password_success_submit(self, driver, random_email, valid_password):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_submit))
        driver.find_element(*self.input_name).send_keys('Kristina')
        driver.find_element(*self.input_email).send_keys(random_email)
        driver.find_element(*self.input_password).send_keys(valid_password)
        driver.find_element(*self.button_submit).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_login))
        # assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        assert expected_conditions.visibility_of_element_located(self.button_register)

    # Регистрация аккаунта при вводе НЕвалидного по длине значения в поле "Пароль"
    @pytest.mark.parametrize('wrong_password', ['12345', '1234', '1', ''])
    def test_registration_invalid_length_password_failed_submit(self, driver, random_email, wrong_password):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_submit))
        driver.find_element(*self.input_name).send_keys('Kristina')
        driver.find_element(*self.input_email).send_keys(random_email)
        driver.find_element(*self.input_password).send_keys(wrong_password)
        driver.find_element(*self.button_submit).click()
        assert expected_conditions.visibility_of_element_located(self.button_submit)

    # Проверка появления подсказки при вводе НЕвалидного по длине значения в поле "Пароль"
    @pytest.mark.parametrize('wrong_password', ['12345', '1234', '1',])
    def test_registration_invalid_length_password_notification_incorrect_password(self, driver, random_email, wrong_password):
        driver.find_element(*self.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_register))
        driver.find_element(*self.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(self.button_submit))
        driver.find_element(*self.input_name).send_keys('Kristina')
        driver.find_element(*self.input_email).send_keys(random_email)
        driver.find_element(*self.input_password).send_keys(wrong_password)
        driver.find_element(*self.button_submit).click()
        assert driver.find_element(*self.notification_incorrect_password).text == 'Некорректный пароль'
