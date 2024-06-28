from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from ..locators import Locators
from ..pages_url import PagesUrl
from ..data import TestData


@pytest.mark.usefixtures("setup_register", "register_data")
class TestRegistration:
    def test_registration(self, register_data):
        self.driver.find_element(By.XPATH, Locators.name).send_keys(register_data[0])
        self.driver.find_element(By.XPATH, Locators.email).send_keys(register_data[1])
        self.driver.find_element(By.XPATH, Locators.password).send_keys(TestData.password)
        self.driver.find_element(By.XPATH, Locators.button_register).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_header)))
        assert self.driver.current_url == PagesUrl.login

    def test_registration_error_password(self, register_data):
        self.driver.find_element(By.XPATH, Locators.name).send_keys(register_data[0])
        self.driver.find_element(By.XPATH, Locators.email).send_keys(register_data[1])
        self.driver.find_element(By.XPATH, Locators.password).send_keys(TestData.invalid_password)
        self.driver.find_element(By.XPATH, Locators.button_register).click()
        assert self.driver.find_element(By.XPATH, Locators.password_error).is_displayed()
        assert self.driver.current_url == PagesUrl.register

