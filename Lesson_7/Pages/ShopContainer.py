from selenium.webdriver.common.by import By


class ShopContainer:
    def __init__(self, browser):
        self.browser = browser
        self.browser.maximize_window()
        self.browser.get("https://www.saucedemo.com/")
# авторизоваться

    def authorization(self):
        self.browser.find_element(
            By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
        self.browser.find_element(
            By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
        self.browser.find_element(By.CSS_SELECTOR, '#login-button').click()
# добавить в корзину товары

    def add_product_to_cart(self):
        self.browser.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.browser.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.browser.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie').click()
# зайти в корзину

    def go_to_cart(self):
        self.browser.find_element(
            By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
# нажать кнопку Checkout

    def press_button_Checkout(self):
        self.browser.find_element(By.ID, 'checkout').click()
# заполнить форму

    def fill_out_form(self):
        fields = {
            "firstName": "Иван",
            "lastName": "Петров",
            "postalCode": "423457"}

        for field_name, value in fields.items():
            field = self.browser.find_element(
                By.CSS_SELECTOR, f"[name='{field_name}']")
            field.send_keys(value)
# нажать кнопку Continue

    def press_button_Continue(self):
        self.browser.find_element(By.ID, 'continue').click()
# прочитать со страницы итоговую стоимость

    def final_cost(self):
        return self.browser.find_element(
            By.CSS_SELECTOR, '[data-test="total-label"]').text
