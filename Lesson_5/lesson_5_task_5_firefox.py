from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

# зайти на сайт в хром и фаирфокс
try:
    firefox.get("http://the-internet.herokuapp.com/inputs")

    # ввести значение
    input_field_firefox = firefox.find_element(By.TAG_NAME, "input")
    input_field_firefox.send_keys("1000")
    sleep(2)
    # удалить значение
    input_field_firefox.clear()
    sleep(1)
    # ввести новое значение
    input_field_firefox.send_keys("999")
    sleep(1)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
