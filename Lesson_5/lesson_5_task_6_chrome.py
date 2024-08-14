from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

# зайти на сайт в хром и фаирфокс
try:
    chrome.get("https://the-internet.herokuapp.com/login")

    # ввести логин
    input_name_chrome = chrome.find_element(
        By.ID, "username").send_keys("tomsmith")
    sleep(2)
    # ввести пароль
    input_pass_chrome = chrome.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(2)
    # нажать кнопку "Login"
    button = chrome.find_element(By.TAG_NAME, "button").click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
