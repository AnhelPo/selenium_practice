"""
https://stepik.org/lesson/732069/step/7?thread=solutions&unit=733602

1. Открыть ссылку.
2. На сайте есть блок с бесконечной подгрузкой чекбоксов. Всего 100 контейнеров и в каждом контейнере 10 чекбоксов.
Отметить только чекбоксы с чётным значением атрибута value.
3. После установки всех чекбоксов во всех контейнерах появится кнопка alert с классом alert_button, нажать на неё.
4. Вывести на экран число из alert-окна.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.7/4/index.html"


class Locators:
    checkbox = By.CSS_SELECTOR, "input[type='checkbox']"
    check_button = By.CLASS_NAME, "alert_button"
    main_container = By.ID, "main_container"


def checkbox_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)

        main_container = ScrollOrigin.from_element(
            browser.find_element(*Locators.main_container))
        actions = ActionChains(browser, duration=100)
        for _ in range(10):
            actions.scroll_from_origin(main_container, 0, 8000).perform()

        for box in browser.find_elements(*Locators.checkbox):
            if not int(box.get_attribute('value')) % 2:
                box.click()
        browser.find_element(*Locators.check_button).click()
        return browser.switch_to.alert.text


print(checkbox_quiz())
