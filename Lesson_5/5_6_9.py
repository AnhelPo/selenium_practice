"""
https://stepik.org/lesson/732063/step/9?unit=733596

1. Открыть ссылку.
2. На странице находятся 100 текстовых полей: 50 серых и 50 синих. Задача — перенести числа из серых полей в синие.
После каждого переноса нажать кнопку "Проверить".
3. Нажать общую кнопку "Проверить".
4. Вывести на экран появившийся код.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://parsinger.ru/selenium/5.5/4/1.html"


class Locators:
    blocks = By.CLASS_NAME, "parent"
    from_element = By.XPATH, "textarea[@color='gray']"
    to_element = By.XPATH, "textarea[@color='blue']"
    block_check = By.TAG_NAME, "button"
    total_check = By.ID, "checkAll"
    total_code = By.ID, "congrats"


# Вариант 1, классический

def move_all_numbers_and_get_code_1() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        blocks = browser.find_elements(*Locators.blocks)
        for block in blocks:
            from_element = block.find_element(*Locators.from_element)
            text_from_box = from_element.text
            from_element.clear()
            block.find_element(*Locators.to_element).send_keys(text_from_box)
            block.find_element(*Locators.block_check).click()

        browser.find_element(*Locators.total_check).click()
        return browser.find_element(*Locators.total_code).text


# Вариант 2: ActionChains, CTRL + C, CTRL + V

def move_all_numbers_and_get_code_2() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        blocks = browser.find_elements(*Locators.blocks)
        act = ActionChains(browser, duration=5)
        for block in blocks:
            from_element = block.find_element(*Locators.from_element)
            to_element = block.find_element(*Locators.to_element)
            act \
                .key_down(Keys.CONTROL, from_element) \
                .send_keys('ax') \
                .key_up(Keys.CONTROL) \
                .key_down(Keys.CONTROL, to_element) \
                .send_keys('v') \
                .key_up(Keys.CONTROL) \
                .send_keys(Keys.TAB) \
                .send_keys(Keys.ENTER) \
                .perform()
        act \
            .send_keys(Keys.TAB) \
            .send_keys(Keys.ENTER) \
            .perform()

        return browser.find_element(*Locators.total_code).text


print(move_all_numbers_and_get_code_1())
print(move_all_numbers_and_get_code_2())
