"""
https://stepik.org/lesson/732083/step/9?unit=733616

1. Открыть ссылку.
2. Когда каждый чекбокс рядом с кнопкой перейдет в состояние "checked", нажать на кнопку.
3. Вывести на экран появившийся текст.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/7/index.html"


class Locators:
    checkbox_container = By.CLASS_NAME, "container"
    checkbox_input = By.TAG_NAME, "input"
    checkbox_btn = By.TAG_NAME, "button"
    result = By.ID, "result"


def wait_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        blocks = browser.find_elements(*Locators.checkbox_container)
        for block in blocks:
            checkbox = block.find_element(*Locators.checkbox_input)
            btn = block.find_element(*Locators.checkbox_btn)
            WebDriverWait(browser, 20).until(EC.element_to_be_selected(checkbox))
            btn.click()
        return browser.find_element(*Locators.result).text


print(wait_quiz())
