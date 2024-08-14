from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox()

# зайти на сайт в хром и фаирфокс
try:
    count = 0
    firefox.get("http://uitestingplayground.com/classattr")

    # нажать синюю кнопку 3 раза
    for x in range(3):
        blue_button = firefox.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        count = count + 1
        sleep(1)

    # нажать Ok в диалоговом окне
        firefox.switch_to.alert.accept()
        print(count)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
