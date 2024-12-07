import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from tests.locators import Message
from selenium.webdriver.common.by import By
class TestStellaBurgersEnter:

    def test_enter_1(self, driver): # Вход по кнопке 'Войти в аккаунт'
        email = Constants.EMAIL
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.CORRECT_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text_button = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located(Locators.PLACE_ON_ORDER)).text
        assert reg_text_button == 'Оформить заказ'
        driver.quit()

    def test_enter_2(self,driver): # Вход через кнопку в форме восстановления пароля
        email = Constants.EMAIL
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.RECOVER_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_2).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.CORRECT_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text_button = WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located(Locators.PLACE_ON_ORDER)).text
        assert reg_text_button == 'Оформить заказ'
        driver.quit()

    def test_enter_3(self,driver): # Вход через кнопку в форме регистрации
        email = Constants.EMAIL
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON_NEW).click()
        driver.find_element(*Locators.LOGIN_BUTTON_2).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.CORRECT_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text_button = WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located(Locators.PLACE_ON_ORDER)).text
        assert reg_text_button == 'Оформить заказ'
        driver.quit()

    def test_enter_4(self, driver): # Вход по кнопке 'Личный кабинет'
        email = Constants.EMAIL
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.CORRECT_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text_button = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located(Locators.PLACE_ON_ORDER)).text
        assert reg_text_button == 'Оформить заказ'
        driver.quit()

    def test_personal_account(self,driver,login): #Переход авторизованного пользователя в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        reg_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).text
        assert reg_text == 'Профиль'
        driver.quit()

    def test_transition_constructor(self, driver):  # Переход по клику на "Конструктор"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BURGER).click()
        reg_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.CUSTOM_BURGER)).text
        assert reg_text == 'Соберите бургер'
        driver.quit()


    def test_transition_stella_burgers(self, driver):# Переход по клику на лого 'Stella Burgers'
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO_STELLA).click()
        reg_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.CUSTOM_BURGER)).text
        assert reg_text == 'Соберите бургер'
        driver.quit()



    def test_exit_account(self,driver,login):  # Выход личного кабинета
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located(Locators.EXIT_ACCOUNT_BUTTON)).click()
        reg_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Message.REGISTRATION_OK)).text
        assert reg_text == 'Вход'
        driver.quit()
