from selenium.webdriver.common.by import By

class MainPageLocators():
    """
    Локаторы главной страницы
    """
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    """
    Локаторы страницы Логина/Регистрации
    """
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTION_EMAIL_STRING = (By.ID, 'id_registration-email')
    REGISTION_PASSWORD_STRING = (By.ID, 'id_registration-password1')
    REGISTION_REPEATED_PASSWORD_STRING = (By.ID, 'id_registration-password2')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    """
    Локаторы страницы продукта
    """
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    CONFIRMATION_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    CONFIRMATION_PRICE_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(2) strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')

class BasePageLocators():
    """
    Универсальные локаторы (можно вызвать на любой странице)
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class BasketPageLocators():
    """
    Локаторы корзины товаров
    """
    BASKET_PRODUCTS = (By.CSS_SELECTOR, '.basket-title.hidden-xs')
    BASKET_PRODUCTS_TEXT = (By.CSS_SELECTOR, '#content_inner > p')


