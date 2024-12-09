import pytest
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


@pytest.fixture(scope='class')
def open_home_page():
    wd = webdriver.Chrome()
    wd.maximize_window()
    wd.get(Constants.URL)
    yield wd
    wd.quit()


@pytest.fixture()
def login(open_home_page):
    email = Constants.USER_MAIL
    open_home_page.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    open_home_page.find_element(*Locators.EMAIL).send_keys(email)
    open_home_page.find_element(*Locators.PASSWORD).send_keys(Constants.CORRECT_PASSWORD)
    open_home_page.find_element(*Locators.LOGIN_BUTTON).click()

@pytest.fixture(scope='function')
def back_to_home_page(open_home_page,request):
    def fin():
        open_home_page.find_element(*Locators.CONSTRUCTOR_BURGER).click()
    request.addfinalizer(fin)
    return open_home_page

@pytest.fixture(scope='function')
def logout(open_home_page,request):
    def fin():
        open_home_page.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(open_home_page, 4).until(EC.visibility_of_element_located(Locators.EXIT_ACCOUNT_BUTTON)).click()
        try:
            open_home_page.find_element(*Locators.CONSTRUCTOR_BURGER).click()
        except ElementClickInterceptedException:
            pass
    request.addfinalizer(fin)
    return open_home_page

