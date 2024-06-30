import pytest
from selenium import webdriver
from .pages_url import PagesUrl
from .locators import Locators
from .data   import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random


@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome()
    driver.get(PagesUrl.domain)
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.fixture()
def login(driver):
    driver.get(PagesUrl.domain + PagesUrl.login_path)
    driver.find_element(By.XPATH, Locators.email).send_keys(TestData.email)
    driver.find_element(By.XPATH, Locators.password).send_keys(TestData.password)
    driver.find_element(By.XPATH, Locators.login_main).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.create_order_button)))
    return driver


@pytest.fixture
def register_data():
    name = f"Любовь{random.randint(1000, 9999)}"
    email = f"polonskaya{random.randint(1000, 9999)}@yandex.ru"
    return name, email



