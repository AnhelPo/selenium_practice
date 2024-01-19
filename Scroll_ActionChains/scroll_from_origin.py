"""
https://stepik.org/lesson/732069/step/4?unit=733602

1. Открыть ссылку.
2. На сайте 5 разных окон, в каждом из которых подгружается по 100 элементов при скроллинге. Для каждого окна нужно
прокрутить страницу до самого низа.
3. Из каждого окна нужно извлечь все числовые значения и сложить их.
4. Вывести на экран общую сумму чисел.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_sum_from_frame(browser, frame_num):
    """Возвращает сумму чисел из списка с заданным номером"""

    scroll_container = browser.find_element(By.XPATH, f'//div[@id="scroll-container_{frame_num}"]/div')
    scroll_origin = ScrollOrigin.from_element(scroll_container)

    for _ in range(6):
        ActionChains(browser) \
            .scroll_from_origin(scroll_origin, 0, 1000) \
            .perform()

        WebDriverWait(browser, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, f'spinner_{frame_num}')))

    numbers = browser.find_elements(By.XPATH, f'//div[@id="scroll-container_{frame_num}"]/span')
    return sum(int(i.text) for i in numbers)


URL = 'http://parsinger.ru/infiniti_scroll_3/'

with webdriver.Chrome() as browser:
    browser.get(URL)
    res = 0
    for frame_num in range(1, 6):
        res += get_sum_from_frame(browser, frame_num)

    print(res)
