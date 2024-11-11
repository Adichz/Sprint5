from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
button_ch = driver.find_element(*TestLocators.BUTTON_CHANGE)
button_ch.click()

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
driver.quit()