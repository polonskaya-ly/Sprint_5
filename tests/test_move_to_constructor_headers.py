from selenium.webdriver.common.by import By
import pytest

from ..locators import Locators

@pytest.mark.usefixtures("setup_main")
class TestMoveToConstructorHeaders:
    def test_move_to_constructor_headers_sauce(self):

        self.driver.find_element(By.XPATH, Locators.sauce_button).click()

        header_main = self.driver.find_element(By.XPATH, Locators.active_constructor_header)

        assert header_main.text == "Соусы"

    def test_move_to_constructor_headers_topping(self):

        self.driver.find_element(By.XPATH, Locators.topping_button).click()

        header_main = self.driver.find_element(By.XPATH, Locators.active_constructor_header)

        assert header_main.text == "Начинки"

    def test_move_to_constructor_headers_bread(self):

        self.driver.find_element(By.XPATH, Locators.topping_button).click()

        self.driver.find_element(By.XPATH, Locators.bread_button).click()

        header_main = self.driver.find_element(By.XPATH, Locators.active_constructor_header)

        assert header_main.text == "Булки"







