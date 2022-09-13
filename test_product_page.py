import pytest
from .pages.product_page import ProductPage
import time

@pytest.mark.parametrize(
    'promo',
    [
        pytest.param(x, marks=pytest.mark.xfail) if x == 7 else x for x in range(5,8)
    ]
)
def test_guest_can_add_product_to_basket(browser,promo):
    # LINK = 'http://selenium1py.pythonanywhere.com' \
    #        '/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # LINK = 'http://selenium1py.pythonanywhere.com' \
    #        '/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    LINK = f'http://selenium1py.pythonanywhere.com' \
           f'/catalogue/coders-at-work_207/?promo=offer{promo}'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.add_product_in_cart()
    product_page.solve_quiz_and_get_code()
    product_page.does_the_name_match()
    product_page.does_the_price_match()

@pytest.mark.xfail(reason="Известная нам ошибка.")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    LINK = f'http://selenium1py.pythonanywhere.com' \
           f'/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.add_product_in_cart()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    LINK = f'http://selenium1py.pythonanywhere.com' \
           f'/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason="Известная нам ошибка.")
def test_message_disappeared_after_adding_product_to_basket(browser):
    LINK = f'http://selenium1py.pythonanywhere.com' \
           f'/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.add_product_in_cart()
    product_page.dissappeared_success_message()