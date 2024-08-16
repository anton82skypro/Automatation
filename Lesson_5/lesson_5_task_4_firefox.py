from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox = webdriver.Firefox()

# зайти на сайт в хром и фаирфокс
try:
    firefox.get("https://the-internet.herokuapp.com/entry_ad")

    # ожидаем кликабельности кнопки и появления модального окна
    wait = WebDriverWait(firefox, 10)
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal')))
    close_buton = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.modal-footer')))
    sleep(3)

    # нажимаем кнопку "Закрыть" в модальном окне
    close_buton.click()
    sleep(1)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
