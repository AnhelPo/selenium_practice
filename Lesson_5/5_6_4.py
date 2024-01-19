"""
https://stepik.org/lesson/732063/step/4?unit=733596

1. Открыть ссылку.
2. За 5 секунд очистить все поля, которые доступны для редактирования.
3. Нажать на кнопку "Проверить".
4. Вывести на экран код из всплывающего алерт-окна.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.5/2/1.html"

with webdriver.Chrome() as browser:
    browser.get(URL)
    fields = browser.find_elements(By.XPATH, "//input[@data-enabled]")
    for field in fields:
        field.clear()
    browser.find_element(By.ID, "checkButton").click()
    print(browser.switch_to.alert.text)
