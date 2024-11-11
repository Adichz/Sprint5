from selenium.webdriver.common.by import By
from selenium import webdriver


class TestLocators:
    BUTTON_LC = [By.XPATH, '/html/body/div/div/header/nav/a']# Кнопка Личный Кабинет
    ENTER_BUTTON_LC = [By.XPATH, ".//button[text()='Войти']"]# Кнопка Войти в Личном Кабинете
    BRED_BUTTON = [By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]']# Кнопка Булки
    SOUS_BUTTON = [By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]']# Кнопка Соусы
    TOPP_BUTTON = [By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]']# Кнопка Топпинги
    PWD_FGT_BUTTON = [By.XPATH, '/html/body/div/div/main/div/div/p[2]/a']#
    QUIT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]# Кнопка Выход из Личного Кабинета
    BUTTON_CHANGE = [By.XPATH, "/html/body/div/div/main/section[2]/div/button"]# Кнопка Войти в аккаунт на главной стрнице
    CONSTRUCTOR_BUTTON = [By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p"]# Кнопка конструктор
    LOGO_BUTTON = [By.XPATH, "/html/body/div/div/header/nav/div/a"]# Кнопка логотипа
    REG_BUTTON = [By.XPATH, "/html/body/div/div/main/div/div/p[1]/a"]# Кнопка Зарегистрироваться в Личном кабинете
    ZAREG_BUTTON = [By.XPATH, "/html/body/div/div/main/div/form/button"]#Кнопка Зарегистрироваться в форме регистрации
    RECOVERY_BUTTON_IN_FORM = [By.XPATH, "/html/body/div/div/main/div/div/p[2]/a"]# Кнопка Восстановить пароль в личном кабинете