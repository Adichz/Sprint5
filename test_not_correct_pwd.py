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
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys('Andre')
button_enter = driver.find_element(*TestLocators.ENTER_BUTTON_LC)
button_enter.click()
time.sleep(1)

assert driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/p").text == 'Некорректный пароль'
driver.quit()