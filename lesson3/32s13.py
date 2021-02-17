import unittest
from selenium import webdriver
import math



class Test11(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath(
            "//*[normalize-space(text())='First name*']/following-sibling::input").send_keys("Alex")
        input2 = browser.find_element_by_xpath(
            "//*[normalize-space(text())='Last name*']/following-sibling::input").send_keys("Domnin")
        input3 = browser.find_element_by_xpath(
            "//*[normalize-space(text())='Email*']/following-sibling::input").send_keys("gog@ya.ru")
        button = browser.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt, 'Text ne sovpadaet')
    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath(
            "//*[normalize-space(text())='First name*']/following-sibling::input").send_keys("Alex")
        input2 = browser.find_element_by_xpath(
            "//*[normalize-space(text())='Last name*']/following-sibling::input").send_keys("Domnin")
        input3 = browser.find_element_by_xpath(
            "//*[normalize-space(text())='Email*']/following-sibling::input").send_keys("gog@ya.ru")
        button = browser.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt, 'Text ne sovpadaet')
if __name__ == "__main__":
    unittest.main()