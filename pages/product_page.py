from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_in_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def do_the_element_match(self):
        self.does_the_name_math()

    def does_the_name_match(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        conf_product_name = self.browser.find_element\
            (*ProductPageLocators.CONFIRMATION_NAME_PRODUCT).text
        assert product_name.lower() == conf_product_name.lower(), 'Элементы не равны или не найдены'

    def does_the_price_match(self):
        product_price = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        conf_product_price = self.browser.find_element\
            (*ProductPageLocators.CONFIRMATION_NAME_PRODUCT).text
        assert product_price.lower() == conf_product_price.lower(), 'Элементы не равны либо не найдены'