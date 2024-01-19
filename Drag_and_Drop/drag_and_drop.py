"""
https://stepik.org/lesson/897512/step/11?thread=solutions&unit=1066949

1. Открыть ссылку.
2. Перенести каждый шарик в соответствующий ему по цвету блок.
3. Вывести на экран полученный код.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.10/4/index.html"


class Locators:
    source = By.CLASS_NAME, "ball_color"
    target = By.CLASS_NAME, "basket_color"
    message = By.CLASS_NAME, "message"


def drag_and_drop_quiz() -> str:
    options = Options()
    options.add_argument("--start-maximized")
    with webdriver.Chrome(options=options) as browser:
        browser.get(URL)
        sources = browser.find_elements(*Locators.source)
        targets = browser.find_elements(*Locators.target)

        target_dict = {}
        for target in targets:
            color = target.value_of_css_property('background-color')
            target_dict[color] = target

        action = ActionChains(browser, duration=2)
        for source in sources:
            color = source.value_of_css_property('background-color')
            target = target_dict[color]
            action \
                .drag_and_drop(source, target) \
                .release() \
                .perform()
        return browser.find_element(*Locators.message).text


print(drag_and_drop_quiz())
