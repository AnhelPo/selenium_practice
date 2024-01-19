"""
https://stepik.org/lesson/732079/step/7?thread=solutions&unit=733612

1. Открыть ссылку.
2. Нажимая на каждую из 10 кнопок, переходить на другие вкладки. В каждой новой вкладке в title число. Нужно собрать
все 10 чисел и сложить их.
3. Вывести на экран полученное число.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://parsinger.ru/blank/3/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    original_handle = browser.current_window_handle

    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for button in buttons:
        button.click()
    WebDriverWait(browser, 1).until(EC.number_of_windows_to_be(11))

    res = 0
    for handle in browser.window_handles:
        if handle != original_handle:
            browser.switch_to.window(handle)
            res += int(browser.title)

    print(res)
