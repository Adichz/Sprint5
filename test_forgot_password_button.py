import time
from selenium.webdriver.common.by import By
from selenium import webdriver


from Locators import TestLocators

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

button_lc = driver.find_element(*TestLocators.BUTTON_LC)
button_lc.click()
time.sleep(1)
pwd_fgt_button = driver.find_element(*TestLocators.PWD_FGT_BUTTON)
pwd_fgt_button.click()
time.sleep(1)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'
driver.quit()