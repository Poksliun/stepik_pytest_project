from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.add_product_in_cart()
    product_page.solve_quiz_and_get_code()
    product_page.does_the_name_match()
