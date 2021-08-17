import time

Link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_last(browser):
    browser.get(Link)
    time.sleep(5)
    browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    print()
