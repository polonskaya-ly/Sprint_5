from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/register")


# Найди поле "Имя" и заполни его
driver.find_element(By.XPATH, '//label[contains(text(), "Имя")]/parent::div/input').send_keys(f"Любовь{random.randint(1000, 9999)}")

# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/parent::div/input').send_keys(f"polonskaya{random.randint(1000, 9999)}@yandex.ru")
# Найди поле "Пароль" и заполни его
driver.find_element(By.XPATH, './/input[@name = "Пароль"]').send_keys('111111')

# Найди кнопку "Зарегистрироваться" и кликни по ней
driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text() = 'Вход']")))

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()

# Получение ошибки для невалидного пароля
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/register")


# Найди поле "Имя" и заполни его
driver.find_element(By.XPATH, '//label[contains(text(), "Имя")]/parent::div/input').send_keys(f"Любовь{random.randint(1000, 9999)}")

# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/parent::div/input').send_keys(f"polonskaya{random.randint(1000, 9999)}@yandex.ru")
# Найди поле "Пароль" и заполни его
driver.find_element(By.XPATH, './/input[@name = "Пароль"]').send_keys('11111')

driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()


WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class = 'input__error text_type_main-default']")))

error_message = driver.find_element(By.XPATH, "//p[@class = 'input__error text_type_main-default']")

assert error_message.text == 'Некорректный пароль'

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

driver.quit()
