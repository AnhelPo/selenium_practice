"""
https://stepik.org/lesson/732083/step/8?unit=733616

1. Открыть ссылку.
2. Дождаться момента, когда чек бокс активируется, и нажать на кнопку "Проверить".
3. Вывести на экран появившийся текст.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/6/index.html"


class Locators:
    checkbox = By.ID, "myCheckbox"
    check_btn = By.TAG_NAME, "button"
    result = By.ID, "result"


def wait_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        WebDriverWait(browser, 2).until(EC.element_located_to_be_selected(Locators.checkbox))
        browser.find_element(*Locators.check_btn).click()
        return browser.find_element(*Locators.result).text


print(wait_quiz())
