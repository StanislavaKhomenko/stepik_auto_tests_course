from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

time.sleep(1)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value").text

y = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)

submit_button = browser.find_element(By.TAG_NAME, "button")
submit_button.click()
