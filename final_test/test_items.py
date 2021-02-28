
link = "http://selenium1py.pythonanywhere.com/catalogue/coder66s-at-work_207/"

def test_button_pass(browser):
    browser.get(link)
    markettext = len(browser.find_elements_by_xpath("//*[@id='add_to_basket_form']/button[@type='submit']"))
    assert markettext > 0, \
        "Buttons add to cart, not on site"