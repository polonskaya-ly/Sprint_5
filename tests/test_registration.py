from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import pytest
from ..locators import Locators


@pytest.mark.usefixtures("setup_register")
class TestRegistration:
    def test_registration(self):

        self.driver.find_element(By.XPATH, Locators.name).send_keys(f"Любовь{random.randint(1000, 9999)}")

        self.driver.find_element(By.XPATH, Locators.email).send_keys(f"polonskaya{random.randint(1000, 9999)}@yandex.ru")

        self.driver.find_element(By.XPATH, Locators.password).send_keys('111111')

        self.driver.find_element(By.XPATH, Locators.button_register).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_header)))

        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_error_password(self):

        self.driver.find_element(By.XPATH, Locators.name).send_keys(f"Любовь{random.randint(1000, 9999)}")

        self.driver.find_element(By.XPATH, Locators.email).send_keys(f"polonskaya{random.randint(1000, 9999)}@yandex.ru")

        self.driver.find_element(By.XPATH, Locators.password).send_keys('11111')

        self.driver.find_element(By.XPATH, Locators.button_register).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.password_error)))

        error_message = self.driver.find_element(By.XPATH, Locators.password_error)

        assert error_message.text == 'Некорректный пароль'

        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

