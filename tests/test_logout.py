from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from ..locators import Locators


class TestLogout:
    @pytest.mark.usefixtures("setup_login")
    def test_logout(self):

        self.driver.find_element(By.XPATH, Locators.email).send_keys("polonskaya2222@yandex.ru")

        self.driver.find_element(By.XPATH, Locators.password).send_keys('222222')

        self.driver.find_element(By.XPATH, Locators.login_main).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile)))

        self.driver.find_element(By.XPATH, Locators.logout).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_header)))

        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


