from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > [value="Добавить в корзину"]')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    CONFIRMATION_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    CONFIRMATION_PRICE_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(2) strong")