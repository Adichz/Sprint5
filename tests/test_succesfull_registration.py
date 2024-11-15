import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators
from tests.conftest import email

main_url = "https://stellarburgers.nomoreparties.site/"
def test_registration_success(driver, email):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
    driver.find_element(*TestLocators.REG_BUTTON).click()
    driver.find_element(*TestLocators.NAME_INPUT_REG).send_keys("Andrey")
    driver.find_element(*TestLocators.EMAIL_INPUT_REG).send_keys(email)
    driver.find_element(*TestLocators.PWD_INPUT_REG).send_keys('Andrey10')
    driver.find_element(*TestLocators.ZAREG_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text()='Восстановить пароль']")))
    driver.find_element(*TestLocators.EMAIL_INPUT_ENTER).send_keys(email)
    driver.find_element(*TestLocators.PWD_INPUT_ENTER).send_keys('Andrey10')
    driver.find_element(*TestLocators.ENTER_BUTTON_LC).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text()='Булки']")))

    assert driver.find_element(*TestLocators.BUTTON_CHANGE).text == 'Оформить заказ'



def test_not_correct_pwd(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_ENTER).send_keys('Andrey_Cheremiskin_16@yandex.ru')
    driver.find_element(*TestLocators.PWD_INPUT_ENTER).send_keys('Andre')
    driver.find_element(*TestLocators.ENTER_BUTTON_LC).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text()='Некорректный пароль']")))
    assert driver.find_element(*TestLocators.NOT_CORRECT_PWD_MSG).text == 'Некорректный пароль'




