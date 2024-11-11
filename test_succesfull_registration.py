import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
button_lc = driver.find_element(*TestLocators.BUTTON_LC)
button_lc.click()
time.sleep(2)
reg_button = driver.find_element(*TestLocators.REG_BUTTON)
reg_button.click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('Andrey')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys('Andrey_Cheremiskin_15@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys('Andrey15')
zareg_button = driver.find_element(*TestLocators.ZAREG_BUTTON)
zareg_button.click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('Andrey_Cheremiskin_15@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys('Andrey15')
button_enter = driver.find_element(*TestLocators.ENTER_BUTTON_LC)
button_enter.click()
time.sleep(1)
button_change = driver.find_element(*TestLocators.BUTTON_CHANGE)
assert button_change.text == 'Оформить заказ'

driver.quit()
