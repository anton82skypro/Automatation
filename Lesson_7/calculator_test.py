import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.homework import URL2


@pytest.mark.test_calculator
def test_calculator(chrome_browser):
    chrome_browser.get(URL2)
    # ввести время ожидания 45 сек
    chrome_browser.find_element(By.CSS_SELECTOR, '#delay').clear()
    chrome_browser.find_element(By.CSS_SELECTOR, '#delay').send_keys("45")
    chrome_browser.find_element(By.CSS_SELECTOR, '.clear').click()
    # ввести 7+8=
    keys = chrome_browser.find_element(By.CSS_SELECTOR, '.keys')
    keys.find_element(By.XPATH, '//span[text()="7"]').click()
    keys.find_element(By.XPATH, '//span[text()="+"]').click()
    keys.find_element(By.XPATH, '//span[text()="8"]').click()
    keys.find_element(By.XPATH, '//span[text()="="]').click()
    start = time.time()
    # ждать появления результата
    waiter = WebDriverWait(chrome_browser, 50)
    waiter.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), "15"))
    stop = time.time()
    # проверить что отобразится результат 15 через 45 секунд
    delta = round(stop - start)
    print(f'delta = {delta}')
    assert delta == 45
