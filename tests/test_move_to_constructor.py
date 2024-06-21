from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Переход по кнопке "Конструктор" из личного кабинета
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/parent::div/input').send_keys("polonskaya2222@yandex.ru")

driver.find_element(By.XPATH, './/input[@name = "Пароль"]').send_keys('222222')

driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

driver.find_element(By.XPATH, ".//a[@href = '/account']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/a[@href="/account/profile"]')))

driver.find_element(By.XPATH, ".//p[contains(text(),'Конструктор')]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

driver.quit()

# Переход по логотипу из личного кабинета
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/parent::div/input').send_keys("polonskaya2222@yandex.ru")

driver.find_element(By.XPATH, './/input[@name = "Пароль"]').send_keys('222222')

driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

driver.find_element(By.XPATH, ".//a[@href = '/account']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/a[@href="/account/profile"]')))

driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

driver.quit()