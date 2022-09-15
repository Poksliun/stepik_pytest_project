import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestOldScripts(unittest.TestCase):
    """
    Проверка выполнение тестов с помощью TestRunner unittest
    """
    def test_firts_path(self):
        #Проверяем тест написанный для первой ссылки, должен выполниться без ошибок
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            time.sleep(1)

            # Ваш код, который заполняет обязательные поля
            inp_list = browser.find_elements(By.TAG_NAME, "input")
            for inputi in inp_list:
                inputi.send_keys('1')


            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_second_path(self):
        #Проверяем тест написанный для второй ссылки, должен выполниться с ошибкой NoSuchElementException
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            time.sleep(1)

            # Ваш код, который заполняет обязательные поля
            fitst_name_input = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
            fitst_name_input.send_keys('Sasha')
            second_name_input = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
            second_name_input.send_keys('Nekrasov')
            email_input = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
            email_input.send_keys('test@xxx.ty')
            time.sleep(1)


            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == '__main__':
    unittest.main()