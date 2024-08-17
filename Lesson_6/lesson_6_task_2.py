from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# зайти на сайт
try:
    driver.get("http://uitestingplayground.com/textinput")

    # ввести текст
    driver.find_element(
        By.CSS_SELECTOR, '#newButtonName').send_keys('SkyPro')

    # нажать кнопку
    driver.find_element(
        By.CSS_SELECTOR, '#updatingButton').click()

    # вывести текст кнопки в консоль
    print(driver.find_element(
        By.CSS_SELECTOR, '#updatingButton').text)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
