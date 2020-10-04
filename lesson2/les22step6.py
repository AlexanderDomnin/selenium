from selenium import webdriver
import time
import math
from Class import print_a,calc

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'
browser.get(link)

try:
    # получаем число
    x = browser.find_element_by_xpath("//*[@id='input_value']").text
    y = calc(x)

    #Ввести ответ
    input1 = browser.find_element_by_xpath("//*[@id='answer']").send_keys(y)
    # Скролл
    button = browser.find_element_by_xpath("//*[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Клики по кнопкам
    check = browser.find_element_by_xpath("//*[@id='robotCheckbox']").click()
    radio = browser.find_element_by_xpath("//*[@id='robotsRule']").click()
    # Подтверждение
    button.click()
    print('Ответ: '+y)
    # Алерт
    print_a(browser)

finally:
    time.sleep(5)
    browser.quit()