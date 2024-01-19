"""
https://stepik.org/lesson/897512/step/13?thread=solutions&unit=1066949

1. Открыть ссылку.
2. На странице 10 слайдеров. Задача - передвинуть каждый слайдер на позицию, указанную в правом столбце.
3. Вывести на экран полученный код.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://parsinger.ru/selenium/5.10/6/index.html"


class Locators:
    slider_container = By.CLASS_NAME, "slider-container"
    slider_input = By.CLASS_NAME, "volume-slider"
    target_value = By.CLASS_NAME, "target-value"
    current_value = By.CLASS_NAME, "current-value"
    message = By.ID, "message"


def drag_and_drop_quiz() -> str:
    options = Options()
    options.add_argument("--start-maximized")
    with webdriver.Chrome(options=options) as browser:
        browser.get(URL)
        containers = browser.find_elements(*Locators.slider_container)
        for container in containers:
            target_input = container.find_element(*Locators.slider_input)
            target_value = int(container.find_element(*Locators.target_value).text)
            current_value = int(container.find_element(*Locators.current_value).text)
            if target_value < current_value:
                key = Keys.ARROW_LEFT
            else:
                key = Keys.ARROW_RIGHT
            diff = abs(target_value - current_value)
            for _ in range(diff):
                target_input.send_keys(key)

        return browser.find_element(*Locators.message).text


print(drag_and_drop_quiz())
