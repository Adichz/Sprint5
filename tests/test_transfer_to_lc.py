import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

main_url = "https://stellarburgers.nomoreparties.site/"
log_url = "https://stellarburgers.nomoreparties.site/login"

def test_transfer_to_lc(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    assert driver.current_url == log_url
