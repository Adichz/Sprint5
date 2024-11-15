import pytest
import time
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield  driver
    driver.quit()
    return driver

@pytest.fixture
def email():
    email = f"andrey_{time.time()}@yandex.ru"
    return email


