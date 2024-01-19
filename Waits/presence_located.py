"""
https://stepik.org/lesson/732083/step/4?thread=solutions&unit=733616

1. Открыть ссылку.
2. На сайте блоки появляются и исчезают. Нужно дождаться блока с ID "qQm9y1rk" и кликнуть по нему.
3. Вывести на экран число из alert-окна.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/2/index.html"


def wait_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        WebDriverWait(browser, 150).until(
            EC.presence_of_element_located((By.ID, "qQm9y1rk"))).click()
        return browser.switch_to.alert.text


print(wait_quiz())
