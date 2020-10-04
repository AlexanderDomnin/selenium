from selenium import webdriver
import time
import math
 # функция
from Class import calc,print_a

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    # Поиск картинки
    img_value = browser.find_element_by_id("treasure").get_attribute("valuex")
    print(img_value)
    y = calc(img_value)
    # Заполняем текстовое поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    #кликаем чекбоксы и баттоны
    checkbox1 = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
    checkbox1.click()
    radiobutton = browser.find_element_by_xpath("//*[@id='robotsRule']")
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