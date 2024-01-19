"""
https://stepik.org/lesson/732063/step/10?unit=733596

1. Открыть ссылку.
2. Получить цвет в формате HEX из каждого элемента <span>.
3. В выпадающем списке в каждом контейнере найти и выберать тот же HEX цвет, что и у родительского контейнера.
4. Найти и нажать на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера.
5. Поставить галочку в чек-боксе на странице.
6. Вставить в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.
7. Нажать на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".
8. Повторить шаги для каждого найденного на странице контейнера.
9. Нажать на кнопку "Проверить все элементы".
10. Вывести на экран код из алерт-окна.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://parsinger.ru/selenium/5.5/5/1.html"


class Locators:
    blocks = By.XPATH, "//span/.."
    block_color = By.TAG_NAME, "span"
    block_select = By.TAG_NAME, "select"
    block_button = lambda color: (By.CSS_SELECTOR, f"button[data-hex='{color}']")
    block_checkbox = By.CSS_SELECTOR, "input[type='checkbox']"
    block_input = By.CSS_SELECTOR, "input[type='text']"
    block_check_btn = By.XPATH, "./button"
    total_check_btn = By.XPATH, "//body/button"


def colors_quiz():
    with webdriver.Chrome() as browser:
        browser.get(URL)
        blocks = browser.find_elements(*Locators.blocks)
        for block in blocks:
            color = block.find_element(*Locators.block_color).text
            Select(block.find_element(*Locators.block_select)).select_by_value(color)
            block.find_element(*Locators.block_button(color)).click()
            block.find_element(*Locators.block_checkbox).click()
            block.find_element(*Locators.block_input).send_keys(color)
            block.find_element(*Locators.block_check_btn).click()

        browser.find_element(*Locators.total_check_btn).click()
        return browser.switch_to.alert.text


print(colors_quiz())
