from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    """
    Класс страницы корзина
    """

    def should_not_be_product_in_the_basket(self):
        #Проверка отсутствия товара в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
            "Отображается сообщение о товаре в корзине, но его не должно быть"

    def checking_the_text_about_an_empty_basket(self):
        #Проверка текста об отсутствии товара в корзине
       assert self.text_comparision(*BasketPageLocators.BASKET_PRODUCTS_TEXT,
                                    'Your basket is empty. Continue shopping'), \
           'Сообщение "Your basket is empty. Continue shopping" не совпадает с сообщением на сайте'
