import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators

def test_transfer_bred():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.SOUS_BUTTON).click()
    driver.find_element(*TestLocators.BRED_BUTTON).click()
    assert driver.find_element(*TestLocators.CURRENT_ELEMENT).text == 'Булки'
    driver.quit()

def test_transfer_sous():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.SOUS_BUTTON).click()
    assert driver.find_element(*TestLocators.CURRENT_ELEMENT).text == 'Соусы'
    driver.quit()

def test_transfer_topp():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestLocators.TOPP_BUTTON).click()
    assert driver.find_element(*TestLocators.CURRENT_ELEMENT).text == 'Начинки'
    driver.quit()
