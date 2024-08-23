import pytest
from selenium.webdriver.common.by import By
from Pages.homework import URL1, fields


def filling_out_the_form(chrome_browser):
    chrome_browser.implicitly_wait(10)
    # зайти на сайт
    chrome_browser.get(URL1)
    # заполнить форму
    for field_name, value in fields.items():
        field = chrome_browser.find_element(
            By.CSS_SELECTOR, f"[name='{field_name}']")
        field.send_keys(value)
    # нажимаем кнопку Submit
    chrome_browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']").click()


@pytest.mark.test_color
# Проверяем статус поля Zip code
def test_danger_color(chrome_browser):
    filling_out_the_form(chrome_browser)
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#zip-code").value_of_css_property("color") == "rgba(132, 32, 41, 1)"

# проверяем статусы полей


def test_success_color(chrome_browser):
    filling_out_the_form(chrome_browser)
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#first-name").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#last-name").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#address").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#e-mail").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#phone").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#city").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#country").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#job-position").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
    assert chrome_browser.find_element(
        By.CSS_SELECTOR,
        "#company").value_of_css_property("color") == "rgba(15, 81, 50, 1)"
