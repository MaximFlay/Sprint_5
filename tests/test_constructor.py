from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from locators import Message


class TestSouse:
    def test_transition_sauce(self, open_home_page, back_to_home_page): # Переход к разделу Соусы
        open_home_page.find_element(*Locators.CONSTRUCTOR_SAUSE).click()
        reg_text = WebDriverWait(open_home_page, 4).until(EC.visibility_of_element_located(Message.TEXT_SAUSE)).text
        assert reg_text == 'Соусы'


class TestFillings:
    def test_transition_filings(self, open_home_page, back_to_home_page):  #Переход к разделу Начинки
        open_home_page.find_element(*Locators.CONSTRUCTOR_FILLINGS).click()
        reg_text = WebDriverWait(open_home_page, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS)).text
        assert reg_text == 'Начинки'


class TestRolls:
    def test_transition_rolls(self, open_home_page, back_to_home_page): # Переход к разделу Булки
        open_home_page.find_element(*Locators.CONSTRUCTOR_FILLINGS).click()
        WebDriverWait(open_home_page, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS))
        open_home_page.find_element(*Locators.CONSTRUCTOR_BUNS).click()
        reg_text = WebDriverWait(open_home_page, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS)).text
        assert reg_text == 'Булки'



