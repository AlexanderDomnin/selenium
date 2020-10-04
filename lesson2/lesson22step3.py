from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from Class import print_a,sum

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'
browser.get(link)

try:
    #Получаем 2 числа
    one = browser.find_element_by_id("num1").text
    two = browser.find_element_by_id("num2").text
    sum1 = sum(one,two)
    # Выбор элемента
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sum1)
    # Подтверждение
    button = browser.find_element_by_xpath("//*[@type='submit']").click()
    print('Сумма: '+sum1)
    # Алерт
    print_a(browser)

finally:
    time.sleep(5)
    browser.quit()