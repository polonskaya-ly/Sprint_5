from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from ..locators import Locators


@pytest.mark.usefixtures("setup_login")
class TestMoveToConstructor:
    def test_move_from_personal_account_through_constructor_button(self):

        self.driver.find_element(By.XPATH, Locators.email).send_keys("polonskaya2222@yandex.ru")

        self.driver.find_element(By.XPATH, Locators.password).send_keys('222222')

        self.driver.find_element(By.XPATH, Locators.login_main).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile)))

        self.driver.find_element(By.XPATH, Locators.constructor).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_move_from_personal_account_through_logo(self):

        self.driver.find_element(By.XPATH, Locators.email).send_keys("polonskaya2222@yandex.ru")

        self.driver.find_element(By.XPATH, Locators.password).send_keys('222222')

        self.driver.find_element(By.XPATH, Locators.login_main).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile)))

        self.driver.find_element(By.CLASS_NAME, Locators.logo).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"
