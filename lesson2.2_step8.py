from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

        
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')
    input1.send_keys("Maxim") 

    input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')
    input2.send_keys("Kurpyakov")

    input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter email"]')
    input3.send_keys("max@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "File22.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, '#file')
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print("Файл находится:", current_dir)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла