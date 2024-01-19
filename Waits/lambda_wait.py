"""
https://stepik.org/lesson/732083/step/7?thread=solutions&unit=733616

1. Открыть ссылку.
2. Нажать на любую из 9 кнопок. Появится рекламное окно, которое нужно закрыть.
3. Скопировать текст на кнопке.
4. Повторить с 8 оставшимися.
5. Склеить текст по порядку с "-" в виде разделителя.
6. Вывести на экран полученную строку.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/5/index.html"


class Locators:
    box_button = By.CLASS_NAME, "box_button"
    close_btn = By.ID, "close_ad"


def wait_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        code_parts = []
        boxes = browser.find_elements(*Locators.box_button)
        ad_close_btn = browser.find_element(*Locators.close_btn)
        for box in boxes:
            box.click()
            ad_close_btn.click()
            WebDriverWait(browser, 10).until(lambda _: box.text != '')
            code_parts.append(box.text)
        return '-'.join(code_parts)


print(wait_quiz())
