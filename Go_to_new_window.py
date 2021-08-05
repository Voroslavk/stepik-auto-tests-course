from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

browser.find_element_by_css_selector('[type="submit"]').click()

new_window = browser.window_handles[1]
old_window = browser.window_handles[0]
browser.switch_to.window(new_window)

value = browser.find_element_by_css_selector('#input_value')
value_text = value.text
y = calc(value_text)

input = browser.find_element_by_css_selector('#answer')
input.send_keys(y)

submitbutton = browser.find_element_by_css_selector('[type="submit"]').click()