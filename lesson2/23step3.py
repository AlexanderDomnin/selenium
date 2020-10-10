from selenium import webdriver
import math
import time
from Class import calc,print_a

b = webdriver.Chrome()
link="http://suninjuly.github.io/alert_accept.html"
b.get(link)

try:
    button=b.find_element_by_xpath("//*[@type='submit']").click()
    confirm = b.switch_to.alert.accept()
    y = b.find_element_by_xpath("//*[@id='input_value']").text
    x = calc(y)
    input = b.find_element_by_xpath("//*[@id='answer']").send_keys(x)
    print('Ответ на задачу: '+x)
    button1=b.find_element_by_xpath("//*[@type='submit']").click()
    print_a(b)
finally:
    time.sleep(5)
    b.quit()