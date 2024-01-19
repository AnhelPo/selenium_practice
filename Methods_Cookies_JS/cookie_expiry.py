"""
https://stepik.org/lesson/732063/step/5?unit=733596

1. Открыть ссылку.
2. Открыть каждую из 42 ссылок. Найти cookie с максимальным сроком жизни (['expiry']).
3. Со страницы с выбранным cookie извлечь число, которое лежит в теге <p id="result">INT</p>.
4. Вывести на экран код из всплывающего алерт-окна.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/methods/5/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    links = browser.find_elements(By.CLASS_NAME, 'urls')
    max_expiry, number = 0, 0
    for link in links:
        link.click()
        cookies = browser.get_cookies()
        expiry = max(int(c['expiry']) for c in cookies)
        if expiry > max_expiry:
            max_expiry = expiry
            number = browser.find_element(By.ID, 'result').text
        browser.back()

    print(number)
