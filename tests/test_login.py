import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators
from tests.conftest import driver


main_url = "https://stellarburgers.nomoreparties.site/"
log_url = "https://stellarburgers.nomoreparties.site/login"

def test_login_account_main(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_CHANGE).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
    assert driver.current_url == log_url

def test_login_from_lc_button(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
    assert driver.current_url == log_url

def test_login_from_reg_form_button(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
    driver.find_element(*TestLocators.REG_BUTTON).click()
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    assert driver.current_url == log_url

def test_login_from_recovery_form_button(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
    driver.find_element(*TestLocators.PWD_FGT_BUTTON).click()
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    assert driver.current_url == log_url

