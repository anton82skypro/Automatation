from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

# зайти на сайт в хром и фаирфокс
try:
    chrome.get("http://the-internet.herokuapp.com/inputs")

    # ввести значение
    input_field_chrome = chrome.find_element(By.TAG_NAME, "input")
    input_field_chrome.send_keys("1000")
    sleep(3)
    # удалить значение
    input_field_chrome.clear()
    sleep(2)
    # ввести новое значение
    input_field_chrome.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
