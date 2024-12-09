from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators
from locators import Message


class TestStellaBurgersEnter:

    def test_enter_click_login_to_account(self, open_home_page, logout): # Вход по кнопке 'Войти в аккаунт'
        email = Constants.USER_MAIL
        password = Constants.CORRECT_PASSWORD
        open_home_page.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        open_home_page.find_element(*Locators.EMAIL).send_keys(email)
        open_home_page.find_element(*Locators.PASSWORD).send_keys(password)
        open_home_page.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text_button = WebDriverWait(open_home_page, 4).until(
        EC.visibility_of_element_located(Locators.PLACE_ON_ORDER)).text
        assert reg_text_button == 'Оформить заказ'

    def test_enter_click_recovery_form(self, open_home_page, logout): # Вход через кнопку в форме восстановления пароля
        email = Constants.USER_MAIL
        password = Constants.CORRECT_PASSWORD
        open_home_page.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        open_home_page.find_element(*Locators.RECOVER_PASSWORD_BUTTON).click()
        open_home_page.find_element(*Locators.LOGIN_BUTTON_2).click()
        open_home_page.find_element(*Locators.EMAIL).send_keys(email)
        open_home_page.find_element(*Locators.PASSWORD).send_keys(password)
        open_home_page.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text_button = WebDriverWait(open_home_page, 4).until(
            EC.visibility_of_element_located(Locators.PLACE_ON_ORDER)).text
        assert reg_text_button == 'Оформить заказ'

    def test_enter_registration_form(self, open_home_page, logout): # Вход через кнопку в форме регистрации
        email = Constants.USER_MAIL
        password = Constants.CORRECT_PASSWORD
        open_home_page.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        open_home_page.find_element(*Locators.REG_BUTTON_NEW).click()
        open_home_page.find_element(*Locators.LOGIN_BUTTON_2).click()
        open_home_page.find_element(*Locators.EMAIL).send_keys(email)
        open_home_page.find_element(*Locators.PASSWORD).send_keys(password)
        open_home_page.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text_button = WebDriverWait(open_home_page, 4).until(
            EC.visibility_of_element_located(Locators.PLACE_ON_ORDER)).text
        assert reg_text_button == 'Оформить заказ'

    def test_enter_personal_account(self, open_home_page, logout): # Вход по кнопке 'Личный кабинет'
        email = Constants.USER_MAIL
        password = Constants.CORRECT_PASSWORD
        open_home_page.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        open_home_page.find_element(*Locators.EMAIL).send_keys(email)
        open_home_page.find_element(*Locators.PASSWORD).send_keys(password)
        open_home_page.find_element(*Locators.LOGIN_BUTTON).click()
        reg_text_button = WebDriverWait(open_home_page, 4).until(
        EC.visibility_of_element_located(Locators.PLACE_ON_ORDER)).text
        assert reg_text_button == 'Оформить заказ'

    def test_personal_account(self, open_home_page, login, logout): #Переход авторизованного пользователя в личный кабинет
        open_home_page.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        reg_text = WebDriverWait(open_home_page, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).text
        assert reg_text == 'Профиль'

    def test_transition_constructor(self, open_home_page, login, logout):  # Переход по клику на "Конструктор"
        open_home_page.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        open_home_page.find_element(*Locators.CONSTRUCTOR_BURGER).click()
        reg_text = WebDriverWait(open_home_page, 3).until(
            EC.visibility_of_element_located(Locators.CUSTOM_BURGER)).text
        assert reg_text == 'Соберите бургер'

    def test_transition_stella_burgers(self, open_home_page, back_to_home_page):# Переход по клику на лого 'Stella Burgers'
        open_home_page.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        open_home_page.find_element(*Locators.LOGO_STELLA).click()
        reg_text = WebDriverWait(open_home_page, 3).until(
            EC.visibility_of_element_located(Locators.CUSTOM_BURGER)).text
        assert reg_text == 'Соберите бургер'

    def test_exit_account(self, open_home_page, login, back_to_home_page):  # Выход личного кабинета
        open_home_page.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(open_home_page, 4).until(EC.visibility_of_element_located(Locators.EXIT_ACCOUNT_BUTTON)).click()
        reg_text = WebDriverWait(open_home_page, 3).until(EC.visibility_of_element_located(Message.REGISTRATION_OK)).text
        assert reg_text == 'Вход'
        
