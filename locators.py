class Locators:
    name = '//label[contains(text(), "Имя")]/parent::div/input'
    email= '//label[contains(text(), "Email")]/parent::div/input'
    password = './/input[@name = "Пароль"]'
    button_register = "//button[contains(text(),'Зарегистрироваться')]"
    enter_header = ".//h2[text() = 'Вход']"
    password_error = "//p[@class = 'input__error text_type_main-default']"
    personal_account_entrance = '//button[contains(text(),"Войти в аккаунт")]'
    create_order_button = './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    login_button = './/a[@href = "/login"]'
    personal_account_button = './/a[@href = "/account"]'
    login_main = ".//button[contains(text(),'Войти')]"
    profile = './/a[@href="/account/profile"]'
    logout = "//button[contains(text(),'Выход')]"
    constructor = ".//p[contains(text(),'Конструктор')]"
    logo = "AppHeader_header__logo__2D0X2"
    sauce_button = ".//span[text() = 'Соусы']"
    active_constructor_header = ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    topping_button = ".//span[text() = 'Начинки']"
    bread_button = ".//span[text() = 'Булки']"