from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    # 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    # 2. Дождаться, когда цена дома уменьшится до $100
    # (ожидание нужно установить не меньше 12 секунд)

    # В объекте WebDriverWait используется функция until,
    # в которую передается правило ожидания, элемент,
    # а также значение, по которому мы будем искать элемент.

    # element_to_be_clickable вернет элемент, когда он станет
    # кликабельным, или вернет False в ином случае.

    # Использован поиск элементов с помощью класса By

    # EC - модуль expected_conditions содержит правила,
    # которые позволяют реализовать необходимые ожидания
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100") )

    # 3. Нажать на кнопку "Book"
    btn = browser.find_element_by_id("book") # Объявляем кнопку
    btn.click() # И прокликиваем


    # Импорт математических функций
    import math

    # Посчитать математическую функцию от x
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Скроллинг страницы вниз
    browser.execute_script("window.scrollBy(0, 150);")

    # Поиск элемента со значением перемнной x
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # Ввод ответа в текстовое поле
    y_element = browser.find_element_by_class_name("form-control")
    y_element.send_keys(y)

    # Нажатие на кнопку "Book"
    button = browser.find_element_by_id("solve") # Объявляем кнопку
    button.click() # И прокликиваем

    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()