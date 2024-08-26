import pytest
import time
from Pages.CalcMainPage import CalcMainPage


@pytest.mark.test_calculator
def test_calculator(chrome_browser):
    calc_main = CalcMainPage(chrome_browser)
    calc_main.insert_time()
    calc_main.clicking_buttons()
    start = time.time()
    calc_main.wait_button_gettext()
    stop = time.time()
    # проверить что отобразится результат 15 через 45 секунд
    delta = round(stop - start)
    print(f'delta = {delta}')
    assert delta == 45
