import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators

def test_login_account_main():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_CHANGE).click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

def test_login_from_lc_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

def test_login_from_reg_form_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    time.sleep(1)
    driver.find_element(*TestLocators.REG_BUTTON).click()
    time.sleep(1)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    time.sleep(1)
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.quit()

def test_login_from_recovery_form_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    time.sleep(1)
    driver.find_element(*TestLocators.PWD_FGT_BUTTON).click()
    time.sleep(1)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    time.sleep(1)
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.quit()
