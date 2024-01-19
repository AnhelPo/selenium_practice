"""
https://stepik.org/lesson/897512/step/12?thread=solutions&unit=1066949

1. Открыть ссылку.
2. На странице 8 кусочков и 8 цветных областей. В каждой области указано расстояние, на которое необходимо переместить
 кусочек, чтобы он оказался в своей области. Когда все кусочки будут на месте, появится код.
3. Вывести на экран полученный код.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.10/8/index.html"


class Locators:
    source = By.CLASS_NAME, "piece"
    target = By.CLASS_NAME, "range"
    message = By.ID, "message"


def drag_and_drop_quiz() -> str:
    options = Options()
    options.add_argument("--start-maximized")
    with webdriver.Chrome(options=options) as browser:
        browser.get(URL)
        sources = browser.find_elements(*Locators.source)
        targets = browser.find_elements(*Locators.target)

        offset_dict = {}
        for target in targets:
            color = target.value_of_css_property('background-color')
            offset_dict[color] = int(target.text.split(': ')[1].strip('px'))

        action = ActionChains(browser, duration=2)
        for source in sources:
            color = source.value_of_css_property('background-color')
            target_offset = offset_dict[color]
            action \
                .drag_and_drop_by_offset(source, target_offset, 0) \
                .release() \
                .perform()
        return browser.find_element(*Locators.message).text


print(drag_and_drop_quiz())
