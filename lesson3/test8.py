import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser...")
    browser=webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()


@pytest.mark.parametrize("stepik",["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_answer_link(browser,stepik):
    link=f"https://stepik.org/lesson/{stepik}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_xpath("//textarea")
    input1.send_keys(answer)
    button = WebDriverWait(browser, 5).until( EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()
    hint = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.TAG_NAME ,"pre")))
    hint_text = hint.text
    assert hint_text == "Correct!", \
        f"{hint_text}"



