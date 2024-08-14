from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

# зайти на сайт в хром и фаирфокс
try:
    firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # нажать Add Element 5 раз
    for x in range(5):
        firefox.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        sleep(1)

    # список кнопок Delete
        firefox_delete_buttons = firefox.find_elements(
            "xpath", '//button[text()="Delete"]')
        print(
            f"Кол-во нажатий кнопок Delete: {len(firefox_delete_buttons)}")

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
