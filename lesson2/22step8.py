
from selenium import webdriver
import os
import time
from Class import print_a

b = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
b.get(link)

try:
    # заполяем поля
    name = b.find_element_by_xpath("//*[@placeholder='Enter first name']").send_keys("Mick")
    sur = b.find_element_by_xpath("//*[@placeholder='Enter last name']").send_keys("Click")
    mail = b.find_element_by_xpath("//*[@placeholder='Enter email']").send_keys("goga@ya.ru")
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, '1.txt')
    print(file_path)
    # прикрепляем файл
    file = b.find_element_by_xpath("//*[@id='file']").send_keys(file_path)
    # Подтверждаем
    button = b.find_element_by_xpath("//*[@type='submit']").click()
    print_a(b)
finally:
    time.sleep(5)
    b.quit()