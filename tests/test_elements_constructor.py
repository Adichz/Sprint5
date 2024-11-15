import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators

main_url = "https://stellarburgers.nomoreparties.site/"

def test_transfer_bred(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.SOUS_BUTTON).click()
    driver.find_element(*TestLocators.BRED_BUTTON).click()
    assert driver.find_element(*TestLocators.CURRENT_ELEMENT).text == 'Булки'

def test_transfer_sous(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.SOUS_BUTTON).click()
    assert driver.find_element(*TestLocators.CURRENT_ELEMENT).text == 'Соусы'

def test_transfer_topp(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.TOPP_BUTTON).click()
    assert driver.find_element(*TestLocators.CURRENT_ELEMENT).text == 'Начинки'
