import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from tests.locators import Message


class TestStellarBurgersRegistration:
    def test_registration(self, driver): # Регистрация пользователя
        email = Constants.EMAIL
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON_NEW).click()
        driver.find_element(*Locators.LOGIN_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.CORRECT_PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()
        reg_text = WebDriverWait(driver,3).until(EC.visibility_of_element_located(Message.REGISTRATION_OK)).text
        assert reg_text == 'Вход'
        driver.quit()

    def test_incorrect_password(self,driver): # Ошибка некорректного пароля
        email = Constants.EMAIL
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON_NEW).click()
        driver.find_element(*Locators.LOGIN_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.INCORRECT_PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()
        incorrect_password = WebDriverWait(driver,4).until(EC.visibility_of_element_located(Message.TEXT_ICORRECT_PSWD)).text
        assert incorrect_password == 'Некорректный пароль'
        driver.quit()

