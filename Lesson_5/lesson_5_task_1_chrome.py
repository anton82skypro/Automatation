from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

# зайти на сайт в хром и фаирфокс
try:
    chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # нажать Add Element 5 раз
    for x in range(5):
        chrome.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        sleep(1)

    # список кнопок Delete
        chrome_delete_buttons = chrome.find_elements(
            "xpath", '//button[text()="Delete"]')
        print(
            f"Кол-во нажатий кнопок Delete: {len(chrome_delete_buttons)}")

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
