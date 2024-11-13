import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators

def test_transfer_to_lc():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()