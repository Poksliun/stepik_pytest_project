from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    """
    Класс страницы продукта
    """

    def add_product_in_cart(self):
        #Добавить товар в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def does_the_element_match(self):
        #Проверка, что цена и название в корзине совпадают с ценой и названием на странцие товара
        self.does_the_name_matсh()
        self.does_the_price_match()

    def does_the_name_matсh(self):
        #Проверка, что название продукта в корзине и на странице одинаковые
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        conf_product_name = self.browser.find_element\
            (*ProductPageLocators.CONFIRMATION_NAME_PRODUCT).text
        assert product_name.lower() == conf_product_name.lower(), 'Элементы не равны или не найдены'

    def does_the_price_match(self):
        #Проверка, что цена продукта в корзине и на странице одинаковые
        product_price = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        conf_product_price = self.browser.find_element\
            (*ProductPageLocators.CONFIRMATION_NAME_PRODUCT).text
        assert product_price.lower() == conf_product_price.lower(), 'Элементы не равны или не найдены'

    def should_not_be_success_message(self):
        #Проверка отсутствия сообщения об удачном добавлении товара
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Отображается сообщение об успешном завершении, но оно его должно быть"

    def dissappeared_success_message(self):
        #Проверка о том, что сообщение об успешном добавлении в корзину пропало
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Сообщение об успешном добавлении не пропало"