import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators


def test_registration_success():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    time.sleep(1)
    driver.find_element(*TestLocators.REG_BUTTON).click()
    time.sleep(1)
    driver.find_element(*TestLocators.NAME_INPUT_REG).send_keys('Andrey')
    driver.find_element(*TestLocators.EMAIL_INPUT_REG).send_keys('Andrey_Cheremiskin_10@yandex.ru')
    driver.find_element(*TestLocators.PWD_INPUT_REG).send_keys('Andrey10')
    driver.find_element(*TestLocators.ZAREG_BUTTON).click()
    time.sleep(1)
    driver.find_element(*TestLocators.EMAIL_INPUT_ENTER).send_keys('Andrey_Cheremiskin_10@yandex.ru')
    driver.find_element(*TestLocators.PWD_INPUT_ENTER).send_keys('Andrey10')
    driver.find_element(*TestLocators.ENTER_BUTTON_LC).click()
    time.sleep(1)
    assert driver.find_element(*TestLocators.BUTTON_CHANGE).text == 'Оформить заказ'
    driver.quit()


def test_not_correct_pwd():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_ENTER).send_keys('Andrey_Cheremiskin_16@yandex.ru')
    driver.find_element(*TestLocators.PWD_INPUT_ENTER).send_keys('Andre')
    driver.find_element(*TestLocators.ENTER_BUTTON_LC).click()
    time.sleep(1)
    assert driver.find_element(*TestLocators.NOT_CORRECT_PWD_MSG).text == 'Некорректный пароль'
    driver.quit()



