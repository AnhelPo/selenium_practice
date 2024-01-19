"""
https://stepik.org/lesson/732069/step/5?unit=733602

1. Открыть ссылку.
2. Кликнуть по каждому объекту на экране (объекты движутся).
3. Вывести на экран число из алерт-окна.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://parsinger.ru/selenium/5.7/1/index.html"


class Locators:
    buttons = By.CSS_SELECTOR, ".button-container > .clickMe"


def scroll_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        buttons = browser.find_elements(*Locators.buttons)
        actions = ActionChains(browser, duration=1)
        for button in buttons:
            actions \
                .scroll_to_element(button) \
                .send_keys_to_element(button, Keys.ENTER) \
                .perform()
        return browser.switch_to.alert.text


print(scroll_quiz())
