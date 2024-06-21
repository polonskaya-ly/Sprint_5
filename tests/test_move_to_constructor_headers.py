from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Переход к разделу "Соусы"
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//h2[contains(text(),"Соусы")]')))

header_main = driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")

assert header_main.text == "Соусы"

driver.quit()

# Переход к разделу "Начинки"
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//h2[contains(text(),"Булки")]')))

header_main = driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")

assert header_main.text == "Начинки"

driver.quit()

# Переход к разделу "Булки"
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click()

driver.find_element(By.XPATH, ".//span[text() = 'Булки']").click()

header_main = driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")

assert header_main.text == "Булки"

driver.quit()






