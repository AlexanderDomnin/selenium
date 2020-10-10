from selenium import webdriver
from Class import calc,print_a
import math
import time

b = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
b.get(link)

try:
    # Нажать на кнопку
    button = b.find_element_by_xpath("//*[@type='submit']").click()
    # Новая вккладка
    new_windows = b.window_handles[1]
    b.switch_to.window(new_windows)
    # Рассчитываем формулу
    y=b.find_element_by_xpath("//*[@id='input_value']").text
    x = calc(y)
    input = b.find_element_by_xpath("//*[@id='answer']").send_keys(x)
    print('Ответ на задачу: '+x)
    # кнопка
    button1 = b.find_element_by_xpath("//*[@type='submit']").click()
    print_a(b)
finally:
    time.sleep(5)
    b.quit()