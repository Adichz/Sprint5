import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators



def test_quit_from_lc_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.BUTTON_LC).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_ENTER).send_keys('Andrey_Cheremiskin_12@yandex.ru')
    driver.find_element(*TestLocators.PWD_INPUT_ENTER).send_keys('Andrey12')
    driver.find_element(*TestLocators.ENTER_BUTTON_LC).click()
    time.sleep(1)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    time.sleep(1)
    driver.find_element(*TestLocators.QUIT_BUTTON).click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()
