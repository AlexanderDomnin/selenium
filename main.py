from selenium import webdriver
import time



try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    assert True


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла