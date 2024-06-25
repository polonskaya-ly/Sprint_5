import pytest
from selenium import webdriver


@pytest.fixture()
def setup_login(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    request.cls.driver = driver

    yield driver
    driver.close()


@pytest.fixture()
def setup_register(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    request.cls.driver = driver

    yield driver
    driver.close()


@pytest.fixture()
def setup_main(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    request.cls.driver = driver

    yield driver
    driver.close()


@pytest.fixture()
def setup_password_recovery(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    request.cls.driver = driver

    yield driver
    driver.close()