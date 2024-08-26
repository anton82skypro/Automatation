from selenium import webdriver
from Pages.MainPage import MainPage
from Pages.ResultPage import ResultPage
from Pages.CartPage import CartPage


def test_cart_counter():
    browser = webdriver.Chrome()  # Открываем браузер
    # Переменная хранит экземпляр класса MainPage
    main_page = MainPage(browser)
    main_page.set_cookie_policy()  # Вызываем метод set_cookie_policy
    main_page.serch("Python")

    result_page = ResultPage(browser)
    # result_page.switch_to_table()  #Используем только в видео
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get()  # Переход на страницу с корзиной
    as_is = cart_page.get_counter()  # Текущее значение счетчика на странице

    assert as_is == to_be  # Сравниваем значения счетчика
    browser.quit()


def test_empty_search():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.serch("no book search term")

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()
    assert msg == "Мы ничего не нашли по вашему запросу! Что делать?"
    browser.quit()
