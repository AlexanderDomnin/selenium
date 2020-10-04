from selenium import webdriver
import time
import math


 # функция
from Class import calc,print_a


try:
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    # Считываем текст
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    # Заполняем текстовое поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    #кликаем чекбоксы и баттоны
    checkbox1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox1.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//*[@type='submit']")
    button.click()
    # выводим результат
    result_text = y
    print('Результат вычислений:'+result_text.split()[-1])
    #Алерт
    print_a(browser)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла