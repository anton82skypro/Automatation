import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.implicitly_wait(10)

# зайти на сайт
driver.maximize_window()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# заполнить форму
fields = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro"
}

for field_name, value in fields.items():
    field = driver.find_element(
        By.CSS_SELECTOR, f"[name='{field_name}']")
    field.send_keys(value)

# Нажимаем кнопку Submit
driver.find_element(
    By.CSS_SELECTOR, "button[type='submit']").click()


@pytest.mark.test_color
# Проверяем статус поля Zip code
def test_danger_color():
    assert driver.find_element(
        By.CSS_SELECTOR, "#zip-code").value_of_css_property("color") == "rgba(132, 32, 41, 1)"
# Проверяем статусы полей
def test_success_color():
    assert driver.find_element(
        By.CSS_SELECTOR, f'#{field_name}').value_of_css_property("color") == "rgba(15, 81, 50, 1)"
