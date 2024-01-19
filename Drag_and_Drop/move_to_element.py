"""
https://stepik.org/lesson/897512/step/7?thread=solutions&unit=1066949

1. Открыть ссылку.
2. Провести синий квадрат через все красные точки, следуя по оси X (слева направо).
3. Вывести на экран полученный токен.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://parsinger.ru/draganddrop/3/index.html'

with webdriver.Chrome() as driver:
    driver.get(URL)
    source_element = driver.find_element(By.ID, "block1")
    target_elements = driver.find_elements(By.CSS_SELECTOR, "div.controlPoint")
    result = driver.find_element(By.XPATH, "//p[@id='message']")

    actions = ActionChains(driver)
    actions.click_and_hold(source_element).perform()
    for target in target_elements:
        actions.move_to_element(target).perform()
    # сходим с последней точки
    actions.move_by_offset(-50, 0).release().perform()

    WebDriverWait(driver, 1).until(lambda x: result.text)
    print(result.text)
