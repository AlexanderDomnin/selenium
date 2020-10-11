from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from Class import calc,print_a
import math
import time


b = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
b.get(link)

try:
    chislo = WebDriverWait(b,12).until(ES.text_to_be_present_in_element((By.ID,'price'),'$100'))
    button = b.find_element_by_xpath("//*[@id='book']").click()
    y = b.find_element_by_xpath("//*[@id='input_value']").text
    x = calc(y)
    print("Ответ на задачу: "+x)
    input = b.find_element_by_xpath("//*[@id='answer']").send_keys(x)
    button1 = b.find_element_by_xpath("//*[@type='submit']").click()
    print_a(b)
finally:
    time.sleep(5)
    b.quit()