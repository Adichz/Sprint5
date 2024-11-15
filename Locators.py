from selenium.webdriver.common.by import By


class TestLocators:
    BUTTON_LC = [By.XPATH, ".//*[text()='Личный Кабинет']"]# Кнопка Личный Кабинет
    ENTER_BUTTON_LC = [By.XPATH, ".//button[text()='Войти']"]# Кнопка Войти в Личном Кабинете
    BRED_BUTTON = [By.XPATH, ".//*[text()='Булки']"]# Кнопка Булки
    SOUS_BUTTON = [By.XPATH, ".//*[text()='Соусы']"]# Кнопка Соусы
    TOPP_BUTTON = [By.XPATH, ".//*[text()='Начинки']"]# Кнопка Начинки
    PWD_FGT_BUTTON = [By.XPATH, ".//*[text()='Восстановить пароль']"]#
    QUIT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]# Кнопка Выход из Личного Кабинета
    BUTTON_CHANGE = [By.XPATH, ".//button[contains(@class,'primary')]"]# Кнопка Войти в аккаунт на главной стрнице
    CONSTRUCTOR_BUTTON = [By.XPATH, ".//*[text()='Конструктор']"]# Кнопка конструктор
    LOGO_BUTTON = [By.XPATH, ".//*[@href='/']"]# Кнопка логотипа
    REG_BUTTON = [By.XPATH, ".//*[text()='Зарегистрироваться']"]# Кнопка Зарегистрироваться в Личном кабинете
    ZAREG_BUTTON = [By.XPATH, ".//*[contains(@class, 'primary') and text()='Зарегистрироваться']"]#Кнопка Зарегистрироваться в форме регистрации
    RECOVERY_BUTTON_IN_FORM = [By.XPATH, ".//*[text()='Восстановить пароль']"]# Кнопка Восстановить пароль в личном кабинете
    EMAIL_INPUT_ENTER = [By.XPATH, ".//input[@name='name']"]# Поле ввода Эмейла в личном кабинете
    PWD_INPUT_ENTER = [By.XPATH, ".//input[@name='Пароль']"]# Поле ввода пароля в личном кабинете
    NAME_INPUT_REG = [By.XPATH, ".//fieldset[1]//input"]# Поле ввода имени в форме регистрации
    EMAIL_INPUT_REG = [By.XPATH, ".//fieldset[2]//input"]# Поле ввода эмейла в форме регистрации
    PWD_INPUT_REG = [By.XPATH, ".//fieldset[3]//input"]# Поле ввода пароля в форме регистрации
    NOT_CORRECT_PWD_MSG = [By.XPATH, ".//*[text()='Некорректный пароль']"]# сообщение Некорректный пароль
    ENTER_BUTTON = [By.XPATH, ".//*[@href='/login']"]# Кнопка Войти
    CURRENT_ELEMENT = [By.XPATH, ".//*[contains(@class, 'current')]"]# Выбранный элемент


