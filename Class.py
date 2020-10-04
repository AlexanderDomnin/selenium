from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    # печать
def print_a(browser):
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print('Код для Степика: ' + alert_text.split()[-1])
