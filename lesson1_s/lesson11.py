from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//*[normalize-space(text())='First name*']/following-sibling::input").send_keys("Alex")
    input2 = browser.find_element_by_xpath("//*[normalize-space(text())='Last name*']/following-sibling::input").send_keys("Domnin")
    input3= browser.find_element_by_xpath("//*[normalize-space(text())='Email*']/following-sibling::input").send_keys("gog@ya.ru")
    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//*[@type='submit']").click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1").text
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text_elt

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла