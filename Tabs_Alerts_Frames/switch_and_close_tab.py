"""
https://stepik.org/lesson/732079/step/8?thread=solutions&unit=733612

1. Открыть каждый сайт из списка в отдельной вкладке.
2. На каждой вкладке найти и отметить чекбокс, получить код.
3. Для каждого полученного кода найдти квадратный корень и суммировать с остальными.
4. Округлить сумму до 9 знаков после запятой.
5. Вывести на экран полученное число.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

URLS = (
    'http://parsinger.ru/blank/1/1.html',
    'http://parsinger.ru/blank/1/2.html',
    'http://parsinger.ru/blank/1/3.html',
    'http://parsinger.ru/blank/1/4.html',
    'http://parsinger.ru/blank/1/5.html',
    'http://parsinger.ru/blank/1/6.html'
)

with webdriver.Chrome() as browser:
    original_handle = browser.current_window_handle
    numbers = set()
    for url in URLS:
        browser.switch_to.new_window('tab')
        browser.get(url)
        browser.find_element(By.TAG_NAME, 'input').click()
        result = browser.find_element(By.ID, 'result').text
        numbers.add(int(result))
        browser.close()
        browser.switch_to.window(original_handle)

    print(round(sum(pow(num, 0.5) for num in numbers), 9))
