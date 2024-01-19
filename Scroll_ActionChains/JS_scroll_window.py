"""
https://stepik.org/lesson/732069/step/1?thread=solutions&unit=733602

1. Открыть ссылку.
2. На сайте 100 чекбоксов. Если кликнуть на чекбокс, может появиться число в теге span.
3. Вывести на экран сумму таких чисел.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/scroll/2/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    height = browser.execute_script('return document.body.scrollHeight')
    browser.execute_script(f'window.scrollTo(0, {height});')
    input_boxes = browser.find_elements(By.CLASS_NAME, 'checkbox_class')
    numbers = set()
    for box in input_boxes:
        box.click()
        box_id = box.get_attribute('id')
        result = browser.find_element(By.ID, f'result{box_id}').text
        if result:
            numbers.add(int(result))

print(sum(numbers))
