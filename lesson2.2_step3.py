from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

link = "https://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    a = num1.text
    b = num2.text
    res = int(a) + int(b)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res)) # ищем элемент с текстом с результатом


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла