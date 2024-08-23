import pytest
from selenium.webdriver.common.by import By
from Pages.homework import URL3


@pytest.mark.test_online_store
def test_total_label(chrome_browser):
    chrome_browser.get(URL3)
    # авторизоваться
    chrome_browser.find_element(
        By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
    chrome_browser.find_element(
        By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
    chrome_browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    # добавить в корзину товары
    chrome_browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-backpack').click()
    chrome_browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    chrome_browser.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    # зайти в корзину
    chrome_browser.find_element(
        By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
    # нажать кнопку Checkout
    chrome_browser.find_element(By.ID, 'checkout').click()
    # заполнить форму
    fields = {
        "firstName": "Иван",
        "lastName": "Петров",
        "postalCode": "423457"}

    for field_name, value in fields.items():
        field = chrome_browser.find_element(
            By.CSS_SELECTOR, f"[name='{field_name}']")
        field.send_keys(value)

    # нажать кнопку Continue
    chrome_browser.find_element(By.ID, 'continue').click()
    # Прочитать со страницы итоговую стоимость
    total_label = chrome_browser.find_element(
        By.CSS_SELECTOR, '[data-test="total-label"]').text
    chrome_browser.quit()

    assert total_label == 'Total: $58.29'
