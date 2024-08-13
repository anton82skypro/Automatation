from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
chrome.set_window_size(640, 480)
firefox.set_window_size(640, 480)

    # зайти на сайт в хром и фаирфокс
try:
    chrome.get("http://the-internet.herokuapp.com/inputs")
    firefox.get("http://the-internet.herokuapp.com/inputs")

    # ввести значение
    input_field_chrome = chrome.find_element(By.TAG_NAME, "input")
    input_field_firefox = firefox.find_element(By.TAG_NAME, "input")
    input_field_chrome.send_keys("1000")
    input_field_firefox.send_keys("1000")
    sleep(3)
    # удалить значение
    input_field_chrome.clear()
    input_field_firefox.clear()
    sleep(2)
    # ввести новое значение
    input_field_chrome.send_keys("999")
    input_field_firefox.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()