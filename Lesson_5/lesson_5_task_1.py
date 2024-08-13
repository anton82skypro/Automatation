from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
chrome.set_window_size(640, 480)
firefox.set_window_size(640, 480)
    
    # зайти на сайт в хром и фаирфокс
try:
    chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # нажать Add Element 5 раз
    for x in range(5):
        add_button = chrome.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        add_button = firefox.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        sleep(1)

    # список кнопок Delete
        chrome_delete_buttons = chrome.find_elements(
            "xpath", '//button[text()="Delete"]')
        firefox_delete_buttons = firefox.find_elements(
            "xpath", '//button[text()="Delete"]')
    
        print(f"Кол-во нажатий кнопок Delete в хроме: {len(chrome_delete_buttons)}")
        print(f"Кол-во нажатий кнопок Delete в фаирфоксе: {len(firefox_delete_buttons)}")

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()