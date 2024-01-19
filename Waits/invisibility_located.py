"""
https://stepik.org/lesson/732083/step/6?unit=733616

1. Открыть ссылку.
2. Дождаться появления баннера, закрыть его, дождаться исчезновения.
3. Нажать появившуюся кнопку.
4. Вывести на экран появившийся текст.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/4/index.html"


class Locator:
    close_btn = By.CLASS_NAME, "close"
    click_me_btn = By.TAG_NAME, "button"
    message = By.ID, "message"


def wait_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        close_btn = browser.find_element(*Locator.close_btn)
        close_btn.click()
        WebDriverWait(browser, 20).until(
            EC.invisibility_of_element_located(close_btn))
        browser.find_element(*Locator.click_me_btn).click()
        return browser.find_element(*Locator.message).text


print(wait_quiz())
