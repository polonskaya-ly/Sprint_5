from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from ..locators import Locators
from ..data import TestData
from ..pages_url import PagesUrl


@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login_account_main_page(self):
        self.driver.find_element(By.XPATH, Locators.personal_account_entrance).click()
        self.driver.find_element(By.XPATH, Locators.email).send_keys(TestData.email)
        self.driver.find_element(By.XPATH, Locators.password).send_keys(TestData.password)
        self.driver.find_element(By.XPATH, Locators.login_main).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.create_order_button)))
        assert  self.driver.find_element(By.XPATH, Locators.create_order_button).is_displayed()

    def test_login_registration_page(self):
        self.driver.get(PagesUrl.domain + PagesUrl.register_path)
        self.driver.find_element(By.XPATH, Locators.login_button).click()
        self.driver.find_element(By.XPATH, Locators.email).send_keys(TestData.email)
        self.driver.find_element(By.XPATH, Locators.password).send_keys(TestData.password)
        self.driver.find_element(By.XPATH, Locators.login_main).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.create_order_button)))
        assert  self.driver.find_element(By.XPATH, Locators.create_order_button).is_displayed()

    def test_login_password_recovery(self):
        self.driver.get(PagesUrl.domain + PagesUrl.recovery_path)
        self.driver.find_element(By.XPATH, Locators.login_button).click()
        self.driver.find_element(By.XPATH, Locators.email).send_keys(TestData.email)
        self.driver.find_element(By.XPATH, Locators.password).send_keys(TestData.password)
        self.driver.find_element(By.XPATH, Locators.login_main).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.create_order_button)))
        assert  self.driver.find_element(By.XPATH, Locators.create_order_button).is_displayed()

    def test_login_personal_account(self):
        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()
        self.driver.find_element(By.XPATH, Locators.email).send_keys(TestData.email)
        self.driver.find_element(By.XPATH, Locators.password).send_keys(TestData.password)
        self.driver.find_element(By.XPATH, Locators.login_main).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.create_order_button)))
        assert  self.driver.find_element(By.XPATH, Locators.create_order_button).is_displayed()
