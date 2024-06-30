from selenium.webdriver.common.by import By
import pytest
from ..locators import Locators

@pytest.mark.usefixtures("driver")
class TestMoveToConstructorHeaders:
    def test_move_to_constructor_headers_sauce(self):
        self.driver.find_element(By.XPATH, Locators.sauce_button).click()
        ingredient_button = self.driver.find_element(By.XPATH, Locators.sauce_button).get_attribute('class')
        assert ingredient_button == Locators.active_constructor_header

    def test_move_to_constructor_headers_topping(self):
        self.driver.find_element(By.XPATH, Locators.topping_button).click()
        ingredient_button = self.driver.find_element(By.XPATH, Locators.topping_button).get_attribute('class')
        assert ingredient_button == Locators.active_constructor_header

    def test_move_to_constructor_headers_bread(self):
        self.driver.find_element(By.XPATH, Locators.topping_button).click()
        self.driver.find_element(By.XPATH, Locators.bread_button).click()
        ingredient_button = self.driver.find_element(By.XPATH, Locators.bread_button).get_attribute('class')
        assert ingredient_button == Locators.active_constructor_header







