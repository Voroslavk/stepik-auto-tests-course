from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
browser.find_element_by_css_selector('[type="submit"]').click()

alert = browser.switch_to.alert
alert.accept()

value = browser.find_element_by_css_selector('#input_value')
value_text = value.text
y = calc(value_text)

input = browser.find_element_by_css_selector('#answer')
input.send_keys(y)

submitbutton = browser.find_element_by_css_selector('[type="submit"]').click()


