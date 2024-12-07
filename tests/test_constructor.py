import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from tests.locators import Message
from selenium.webdriver.common.by import By


class TestConstructor:
    def test_click_sauce(self ,driver): # Переход к разделу Соусы
        driver.find_element(*Locators.CONSTRUCTOR_SAUSE).click()
        reg_text = WebDriverWait(driver, 4).until(EC.visibility_of_element_located(Message.TEXT_SAUSE)).text
        assert reg_text == 'Соусы'
        driver.quit()

    def test_click_filings(self,driver):  #Переход к разделу Начинки
        driver.find_element(*Locators.CONSTRUCTOR_FILLINGS).click()
        reg_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS)).text
        assert reg_text == 'Начинки'
        driver.quit()

