from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Вход по кнопке «Войти в аккаунт» на главной
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]').click()

assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/parent::div/input').send_keys("polonskaya2222@yandex.ru")

driver.find_element(By.XPATH, './/input[@name = "Пароль"]').send_keys('222222')

driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

button_make_order = driver.find_element(By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')

assert  button_make_order.text == "Оформить заказ"

driver.quit()


# Вход через кнопку «Войти» на странице регистрации
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, './/a[@href = "/login"]').click()

assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/parent::div/input').send_keys("polonskaya2222@yandex.ru")

driver.find_element(By.XPATH, './/input[@name = "Пароль"]').send_keys('222222')

driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

button_make_order = driver.find_element(By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')

assert  button_make_order.text == "Оформить заказ"

driver.quit()


# Вход через кнопку в форме восстановления пароля
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

driver.find_element(By.XPATH, './/a[@href = "/login"]').click()

assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/parent::div/input').send_keys("polonskaya2222@yandex.ru")

driver.find_element(By.XPATH, './/input[@name = "Пароль"]').send_keys('222222')

driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

button_make_order = driver.find_element(By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')

assert  button_make_order.text == "Оформить заказ"

driver.quit()


# Вход через кнопку "Личный кабинет"
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, './/a[@href = "/account"]').click()

assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/parent::div/input').send_keys("polonskaya2222@yandex.ru")
driver.find_element(By.XPATH, './/input[@name = "Пароль"]').send_keys('222222')

driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

button_make_order = driver.find_element(By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')

assert  button_make_order.text == "Оформить заказ"

driver.quit()
