import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.ShopContainer import ShopContainer
from time import sleep


@pytest.mark.test_online_store
def test_total_label(chrome_browser: WebDriver):
    shop_total_label = ShopContainer(chrome_browser)
    shop_total_label.authorization()
    shop_total_label.add_product_to_cart()
    shop_total_label.go_to_cart()
    shop_total_label.press_button_Checkout()
    shop_total_label.fill_out_form()
    shop_total_label.press_button_Continue()
    sleep(5)
# проверить что стоимость совпадает

    assert shop_total_label.final_cost() == 'Total: $58.29'
