from selenium.common.exceptions import \
    NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

import math

class BasePage():
    """
    Класс для функций, которые можно использовать на любой странице сайта
    """
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        #Переход на страницу логина
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        #Переход на страницу корзины
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        #Проверка, что элемент исчез со страницы
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        #Проверка, что элемент есть на странице
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        #Проверка, что элемента нет на странице
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        #Перейти по ссылке
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        #Проверка, что пользователь залогинен
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Значок пользователя не отображается," \
                                                                    " вероятно, неавторизованный пользователь"
    def should_be_login_link(self):
        #Проверка наличия кнопки (ссылки) на страницу логина
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка для входа в систему не представлена"

    def solve_quiz_and_get_code(self):
        #Ответ вставляемый в алерт при добавлении товара в корзину
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Ваш код: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("Второго предупреждения не было")

    def text_comparision(self, how, what, required_text):
        #Сравнение двух кусков текста (представленного на странице и введенного самостоятельно в тесте)
        try:
            search_text = self.browser.find_element(how, what).text
            search_text = search_text.strip()

        except NoSuchElementException:
            print('Элемент на странице не найден.')
            return False

        return required_text == search_text








