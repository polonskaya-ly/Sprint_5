from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from ..locators import Locators


class TestLogin:
    @pytest.mark.usefixtures("setup_main")
    def test_login_account_main_page(self):

        self.driver.find_element(By.XPATH, Locators.personal_account_entrance).click()

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        self.driver.find_element(By.XPATH, Locators.email).send_keys("polonskaya2222@yandex.ru")

        self.driver.find_element(By.XPATH, Locators.password).send_keys('222222')

        self.driver.find_element(By.XPATH, Locators.login_main).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

        button_make_order = self.driver.find_element(By.XPATH, Locators.create_order_button)

        assert  button_make_order.text == "Оформить заказ"

    @pytest.mark.usefixtures("setup_register")
    def test_login_registration_page(self):

        self.driver.find_element(By.XPATH, Locators.login_button).click()

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        self.driver.find_element(By.XPATH, Locators.email).send_keys("polonskaya2222@yandex.ru")

        self.driver.find_element(By.XPATH, Locators.password).send_keys('222222')

        self.driver.find_element(By.XPATH, Locators.login_main).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

        button_make_order = self.driver.find_element(By.XPATH, Locators.create_order_button)

        assert  button_make_order.text == "Оформить заказ"

    @pytest.mark.usefixtures("setup_password_recovery")
    def test_login_password_recovery(self):

        self.driver.find_element(By.XPATH, Locators.login_button).click()

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        self.driver.find_element(By.XPATH, Locators.email).send_keys("polonskaya2222@yandex.ru")

        self.driver.find_element(By.XPATH, Locators.password).send_keys('222222')

        self.driver.find_element(By.XPATH, Locators.login_main).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

        button_make_order = self.driver.find_element(By.XPATH, Locators.create_order_button)

        assert  button_make_order.text == "Оформить заказ"

    @pytest.mark.usefixtures("setup_main")
    def test_login_personal_account(self):

        self.driver.find_element(By.XPATH, Locators.personal_account_button).click()

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        self.driver.find_element(By.XPATH, Locators.email).send_keys("polonskaya2222@yandex.ru")
        self.driver.find_element(By.XPATH, Locators.password).send_keys('222222')

        self.driver.find_element(By.XPATH, Locators.login_main).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.create_order_button)))

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

        button_make_order = self.driver.find_element(By.XPATH, Locators.create_order_button)

        assert  button_make_order.text == "Оформить заказ"

