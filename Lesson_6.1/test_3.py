import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# авторизоваться
driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, '#login-button').click()
# добавить в корзину товары
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
# зайти в корзину
driver.find_element(
    By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
# нажать кнопку Checkout
driver.find_element(By.ID, 'checkout').click()
# заполнить форму
fields = {
    "firstName": "Иван",
    "lastName": "Петров",
    "postalCode": "423457"}

for field_name, value in fields.items():
    field = driver.find_element(
        By.CSS_SELECTOR, f"[name='{field_name}']")
    field.send_keys(value)

# нажать кнопку Continue
driver.find_element(By.ID, 'continue').click()
# Прочитать со страницы итоговую стоимость
total_label = driver.find_element(
    By.CSS_SELECTOR, '[data-test="total-label"]').text
driver.quit()


@pytest.mark.test_online_store
def test_total_label():
    assert total_label == 'Total: $58.29'
