
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_basket(browser):
    browser.get(link)
    markettext = len(browser.find_elements_by_xpath("//*[@id='add_to_basket_form']/button[@type='submit']"))
    assert markettext > 0, \
        "Buttons add to cart, not on site"