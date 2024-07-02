from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from ..locators import Locators
from ..pages_url import PagesUrl


@pytest.mark.usefixtures("driver","login")
class TestMoveToConstructor:
    def test_move_from_personal_account_through_constructor_button(self):
        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile)))
        self.driver.find_element(By.XPATH, Locators.constructor).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))
        assert self.driver.current_url == PagesUrl.domain

    def test_move_from_personal_account_through_logo(self):
        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile)))
        self.driver.find_element(By.CLASS_NAME, Locators.logo).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))
        assert self.driver.current_url == PagesUrl.domain
