import pytest
from selenium import webdriver
from locators import TestLocators
import random
import string


# Фикстура веб-драйвера
@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


# Фикстура, генерирующая email с четырьмя рандомными буквами и рандомным числом от 100 до 999 для регистрации
@pytest.fixture
def random_email():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(4)))
    random_email = f'kristina_bragina_5_{random_letters}_{random.randint(100, 999)}@yandex.ru'
    return random_email


# Фикстура, генерирующая пароль с двумя рандомными буквами и рандомным числом от 10 до 99 для регистрации
@pytest.fixture
def random_password():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(2)))
    random_password = f'qwerty_{random_letters}_{random.randint(10, 99)}'
    return random_password


# Фикстура, генерирующая основу email с четырьмя рандомными буквами и рандомным числом от 100 до 999
# для негативных проверок на формат вводимого адреса почты
@pytest.fixture
def invalid_random_email():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(4)))
    email_base = f'kristina_bragina_5_{random_letters}_{random.randint(100, 999)}'
    return email_base


# Фикстура для авторизации с валидной парой log/pass перед тестами
@pytest.fixture
def login(driver):
    driver.find_element(*TestLocators.button_login_in_main).click()
    driver.find_element(*TestLocators.input_email_auth).send_keys('kristina_bragina_6_666@ya.ru')
    driver.find_element(*TestLocators.input_password_auth).send_keys('qwerty')
    driver.find_element(*TestLocators.button_login).click()
