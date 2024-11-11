import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


button_lc = driver.find_element(*TestLocators.BUTTON_LC)
button_lc.click()


driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('Andrey_Cheremiskin_12@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys('Andrey12')
button_enter = driver.find_element(*TestLocators.ENTER_BUTTON_LC)
button_enter.click()
time.sleep(1)
button_lc.click()
time.sleep(1)
quit_button = driver.find_element(*TestLocators.QUIT_BUTTON)
quit_button.click()
time.sleep(1)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
driver.quit()