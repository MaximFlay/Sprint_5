import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(Constants.URL)
    WebDriverWait(browser, 4)
    yield browser
    browser.quit()


@pytest.fixture()
def login(driver):
    email = Constants.EMAIL
    driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(email)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.CORRECT_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver
