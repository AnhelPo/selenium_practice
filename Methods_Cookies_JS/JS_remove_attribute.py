"""
https://stepik.org/lesson/732063/step/2?unit=733596

1. Открыть ссылку.
2. На странице 100 текстовых полей с текстом. Задача — удалить содержимое всех полей. По истечении некоторого времени
 поля и кнопка для проверки становятся недоступными.
3. Нажать на кнопку после полного удаления.
4. После нажатия скопировать число из всплывающего alert-окна и вывести его на экран.

Решение с помощью JS-скрипта.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://parsinger.ru/selenium/5.5/1/1.html"

with webdriver.Chrome() as browser:
    browser.get(URL)

    # ждем, пока поля и кнопка станут недоступными
    WebDriverWait(browser, 20).until(EC.element_attribute_to_include((By.ID, "checkButton"), "disabled"))

    # делаем поля снова доступными, убирая атрибут disabled
    browser.execute_script("""
        buttons = document.getElementsByTagName('input');
        for (let button of buttons) {
        button.removeAttribute('disabled');
        }
        """)

    fields = browser.find_elements(By.TAG_NAME, "input")
    for field in fields:
        field.clear()

    # делаем кнопку снова доступной, убирая атрибут disabled
    browser.execute_script("document.getElementById('checkButton').removeAttribute('disabled');")

    browser.find_element(By.ID, "checkButton").click()
    print(browser.switch_to.alert.text)
