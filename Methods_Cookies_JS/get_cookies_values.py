"""
https://stepik.org/lesson/732063/step/3?unit=733596

1. Открыть ссылку.
2. Суммировать числовые значения cookies с чётными числами после символа "_" в имени.
3. Вывести число на экран.
"""

from selenium import webdriver

URL = 'https://parsinger.ru/methods/3/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    cookies = browser.get_cookies()
    res = []
    for cookie in cookies:
        cookie_num = int(cookie['name'].rsplit('_', maxsplit=1)[1])
        if not cookie_num % 2:
            res.append(int(cookie['value']))
    print(sum(res))
