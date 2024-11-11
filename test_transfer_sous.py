from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import TestLocators



driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
sous_button = driver.find_element(*TestLocators.SOUS_BUTTON)
sous_button.click()
element = driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[contains(@class, 'current')]")

assert element.text == 'Соусы'

driver.quit()