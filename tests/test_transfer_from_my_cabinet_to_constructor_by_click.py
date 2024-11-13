import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators

def test_transfer_from_lc_to_constructor_click():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    time.sleep(1)
    driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_transfer_from_lc_by_logo_click():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    time.sleep(1)
    driver.find_element(*TestLocators.LOGO_BUTTON).click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()