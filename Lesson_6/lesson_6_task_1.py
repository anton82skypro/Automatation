from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(17)

# зайти на сайт
try:
    driver.get("http://uitestingplayground.com/ajax")

    # нажать на синюю кнопку
    driver.find_element(
        By.CSS_SELECTOR, '#ajaxButton').click()

    # вывести текст появившейся надписи в консоль
    content = driver.find_element(
        By.CSS_SELECTOR, '#content')
    print(content.find_element(
        By.CSS_SELECTOR, 'p.bg-success').text)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
