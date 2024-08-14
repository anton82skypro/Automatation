from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

# зайти на сайт в хром и фаирфокс
try:
    firefox.get("https://the-internet.herokuapp.com/login")

    # ввести логин
    input_name_firefox = firefox.find_element(
        By.ID, "username").send_keys("tomsmith")
    sleep(2)
    # ввести пароль
    input_pass_firefox = firefox.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(2)
    # нажать кнопку "Login"
    button = firefox.find_element(By.TAG_NAME, "button").click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
