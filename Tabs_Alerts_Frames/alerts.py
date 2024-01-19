"""
https://stepik.org/lesson/732079/step/2?thread=solutions&unit=733612

1. Открыть ссылку.
2. На сайте находится 100 кнопок. Каждая при нажатии активирует всплывающее alert окно с пин-кодом. Под кнопками
расположено текстовое поле, которое проверяет пин-коды. Задача — ввести пин-код и проверить его. Если пин-код верный,
выпадет секретный код.
3. Вывести на экран код.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://parsinger.ru/blank/modal/3/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)

    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    input_form = browser.find_element(By.ID, 'input')
    button_check = browser.find_element(By.ID, 'check')
    result = browser.find_element(By.ID, 'result')

    for button in buttons:
        button.click()
        alert = WebDriverWait(browser, 1).until(EC.alert_is_present())
        code = alert.text
        alert.accept()
        input_form.send_keys(code)
        button_check.click()
        if result.text != 'Неверный пин-код':
            print(result.text)
            break
