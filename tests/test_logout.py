from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from ..locators import Locators
from ..pages_url import PagesUrl


class TestLogout:
    @pytest.mark.usefixtures("login")
    def test_logout(self):
        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile)))
        self.driver.find_element(By.XPATH, Locators.logout).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_header)))
        assert self.driver.current_url == PagesUrl.login


