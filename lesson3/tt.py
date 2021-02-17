from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "https://stepik.org/lesson/236895/step/1"
browser.get(link)

try:
    browser.implicitly_wait(15)
    input1 = browser.find_element_by_xpath("//textarea")
# input1 = browser.find_element_by_xpath("//div[@data-type='string-quiz']")
    input1.send_keys("answer")
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
# тест для Git
# не забываем оставить пустую строку в конце файла
