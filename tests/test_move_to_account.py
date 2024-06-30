from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from ..locators import Locators
from ..pages_url import PagesUrl


@pytest.mark.usefixtures("driver", "login")
class TestMoveToAccount:
    def test_move_to_account(self):
        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile)))
        assert self.driver.current_url == PagesUrl.domain + PagesUrl.account_profile_path
