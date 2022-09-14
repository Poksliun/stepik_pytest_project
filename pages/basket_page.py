from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_product_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
            "Success message is presented, but should not be"

    def checking_the_text_about_an_empty_basket(self):
       assert self.text_comparision(*BasketPageLocators.BASKET_PRODUCTS_TEXT,
                                    'Your basket is empty. Continue shopping'), \
           'Сообщение "Your basket is empty. Continue shopping" не совпадает с сообщением на сайте'
