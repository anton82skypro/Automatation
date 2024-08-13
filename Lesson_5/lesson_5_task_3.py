from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
chrome.set_window_size(640, 480)
firefox.set_window_size(640, 480)
    
    # зайти на сайт в хром и фаирфокс
try:
    count = 0
    chrome.get("http://uitestingplayground.com/classattr")
    firefox.get("http://uitestingplayground.com/classattr")
    
    # нажать синюю кнопку 3 раза
    for x in range(3):
        blue_button = chrome.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
        blue_button = firefox.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
        count = count + 1
        sleep(2)

    # нажать Ok в диалоговом окне
        chrome.switch_to.alert.accept()
        firefox.switch_to.alert.accept()
        print(count)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()