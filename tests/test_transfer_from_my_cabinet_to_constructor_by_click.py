import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

main_url = "https://stellarburgers.nomoreparties.site/"

def test_transfer_from_lc_to_constructor_click(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text()='Булки']")))
    assert driver.current_url == main_url


def test_transfer_from_lc_by_logo_click(driver):
    driver.get(main_url)
    driver.find_element(*TestLocators.BUTTON_LC).click()
    driver.find_element(*TestLocators.LOGO_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text()='Булки']")))
    assert driver.current_url == main_url
