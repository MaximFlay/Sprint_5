from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators
from locators import Message
from helpers import  Userinfo


class TestStellarBurgersRegistration:
    def test_registration(self, open_home_page, back_to_home_page,): # Регистрация пользователя
        email = Userinfo.email
        password = Userinfo.password
        open_home_page.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        open_home_page.find_element(*Locators.REG_BUTTON_NEW).click()
        open_home_page.find_element(*Locators.LOGIN_NAME).send_keys(Userinfo.username)
        open_home_page.find_element(*Locators.EMAIL).send_keys(email)
        open_home_page.find_element(*Locators.PASSWORD).send_keys(password)
        open_home_page.find_element(*Locators.REG_BUTTON).click()
        reg_text = WebDriverWait(open_home_page, 3).until(EC.visibility_of_element_located(Message.REGISTRATION_OK)).text
        assert reg_text == 'Вход'



    def test_incorrect_password(self, open_home_page, back_to_home_page): # Ошибка некорректного пароля
        email = Userinfo.email
        open_home_page.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        open_home_page.find_element(*Locators.REG_BUTTON_NEW).click()
        open_home_page.find_element(*Locators.LOGIN_NAME).send_keys(Userinfo.username)
        open_home_page.find_element(*Locators.EMAIL).send_keys(email)
        open_home_page.find_element(*Locators.PASSWORD).send_keys(Constants.INCORRECT_PASSWORD)
        open_home_page.find_element(*Locators.REG_BUTTON).click()
        incorrect_password = WebDriverWait(open_home_page, 4).until(EC.visibility_of_element_located(Message.TEXT_ICORRECT_PSWD)).text
        assert incorrect_password == 'Некорректный пароль'


