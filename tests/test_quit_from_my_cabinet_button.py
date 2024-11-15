import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from Locators import TestLocators

main_url = "https://stellarburgers.nomoreparties.site/"
log_url = "https://stellarburgers.nomoreparties.site/login"

def test_quit_from_lc_button(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_ENTER).send_keys('Andrey_Cheremiskin_12@yandex.ru')
    driver.find_element(*TestLocators.PWD_INPUT_ENTER).send_keys('Andrey12')
    driver.find_element(*TestLocators.ENTER_BUTTON_LC).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
    driver.find_element(*TestLocators.BUTTON_LC).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,".//*[text()='Профиль']")))
    driver.find_element(*TestLocators.QUIT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text()='Вход']")))
    assert driver.current_url == log_url

