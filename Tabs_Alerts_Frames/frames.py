"""
https://stepik.org/lesson/732079/step/9?thread=solutions&unit=733612

1. Открыть ссылку.
2. На сайте 9 iframe. В каждом из них скрыта кнопка. Нажать на кнопку в каждом iframe, чтобы получить число.
3. Вставить полученное число в поле для проверки, проверить. Если появится alert, нужное число найдено.
4. Вывести на экран полученное число.
"""

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.8/5/index.html"


class Locators:
    frames = By.CSS_SELECTOR, "iframe[id]"
    block_btn = By.TAG_NAME, "button"
    block_num = By.TAG_NAME, "p"
    code_input = By.TAG_NAME, "input"
    check_button = By.ID, "checkBtn"


def iframes_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        frames = browser.find_elements(*Locators.frames)
        codes = set()
        for frame in frames:
            browser.switch_to.frame(frame)
            browser.find_element(*Locators.block_btn).click()
            codes.add(browser.find_element(*Locators.block_num).text)
            browser.switch_to.default_content()

        input_field = browser.find_element(*Locators.code_input)
        check_btn = browser.find_element(*Locators.check_button)
        for code in codes:
            input_field.send_keys(code)
            check_btn.click()
            try:
                return browser.switch_to.alert.text
            except NoAlertPresentException:
                input_field.clear()
                pass


print(iframes_quiz())
