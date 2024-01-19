"""
https://stepik.org/lesson/732069/step/6?unit=733602

1. Открыть ссылку.
2. Найти четыре кнопки на странице, определить value каждой кнопки. Это время, которое необходимо удерживать кнопку.
3. Удерживать кнопки нужное время.
4. Вывести на экран сообщение из алерт-окна.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.7/5/index.html"


class Locators:
    buttons = By.TAG_NAME, "button"


def hold_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        buttons = browser.find_elements(*Locators.buttons)
        actions = ActionChains(browser, duration=100)
        for button in buttons:
            time_to_hold = float(button.get_attribute('value'))
            actions \
                .click_and_hold(button) \
                .pause(time_to_hold) \
                .release(button) \
                .perform()
        return browser.switch_to.alert.text


print(hold_quiz())
