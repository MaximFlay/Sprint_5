from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "// *[text() = 'Личный Кабинет']") #Кнопка Личный кабинет
    PERSONAL_ACCOUNT = (By.XPATH, "//a[.='Профиль']") # Локатор личного кабинета
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH,"//*[.='Войти в аккаунт']") #Кнопка "Войти в акккаунт" вход на страницу авторизации
    REG_BUTTON_NEW = (By.XPATH,"//*[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться" переход на страницу регистрации
    LOGIN_NAME = (By.XPATH,"//*[.='Имя']/input") # Поле ввода Имя
    EMAIL = (By.XPATH,"//*[.='Email']/input") # Поле ввода  email
    PASSWORD = (By.XPATH, "//*[.='Пароль']/input") # поле ввода Пароль
    REG_BUTTON = (By.XPATH,"//button[.='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    PLACE_ON_ORDER = (By.XPATH, "//button[.='Оформить заказ']") # Кнопка Оформить заказ
    LOGIN_BUTTON = (By.XPATH, "//button[.='Войти']") # Кнопка Вход в окне авторизации
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//*[.='Восстановить пароль']") # Кнопка восстановления пароля
    LOGIN_BUTTON_2 = (By.XPATH, "//*[.='Войти']") # Кнопка "Войти на странице Регистрации и восстановления пароля
    EXIT_ACCOUNT_BUTTON = (By.XPATH, "//button[.='Выход']")  #Кнопка Выход из личного кабинета
    LOGO_STELLA = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']") #Логотип Stella Burgers
    CUSTOM_BURGER = (By.XPATH, "//*[.='Соберите бургер']") # главная страница
    CONSTRUCTOR_BURGER= (By.XPATH, "//p[.='Конструктор']") # Кнопка Конструктор
    CONSTRUCTOR_SAUSE = (By.XPATH, "//*[(@class='text text_type_main-default') and (text()='Соусы')]") # Кнопка Соусы
    CONSTRUCTOR_FILLINGS = (By.XPATH, "//*[(@class='text text_type_main-default') and (text()='Начинки')]") # Кнопка Начинки
    CONSTRUCTOR_BUNS = (By.XPATH, "//*[(@class='text text_type_main-default') and (text()='Булки')]") # Кнопка Булки


class Message:
    TEXT_ICORRECT_PSWD = (By.XPATH,"//*[text()='Некорректный пароль']") # Текст при вводе некорректного пароля
    REGISTRATION_OK = (By.XPATH,"//*[.='Вход']")
    TEXT_SAUSE = (By.XPATH, "//h2[contains(text(),'Соусы')]")





