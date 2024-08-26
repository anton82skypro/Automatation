from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcMainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.maximize_window()
        URL2 = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.browser.get(URL2)
# ввести время ожидания 45 сек

    def insert_time(self):
        self.browser.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.browser.find_element(By.CSS_SELECTOR, '#delay').send_keys("45")
        self.browser.find_element(By.CSS_SELECTOR, '.clear').click()
# ввести 7+8=

    def clicking_buttons(self):
        self.browser.find_element(By.XPATH, '//span[text()="7"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="+"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="8"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="="]').click()
# ждать появления результата

    def wait_button_gettext(self):
        WebDriverWait(self.browser, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))
