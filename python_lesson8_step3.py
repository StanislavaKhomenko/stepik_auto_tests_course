from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

first_name = browser.find_element(By.NAME, "firstname")
first_name.click()
first_name.send_keys("Stasya")

last_name = browser.find_element(By.NAME, "lastname")
last_name.click()
last_name.send_keys("Khom")

email = browser.find_element(By.NAME, "email")
email.click()
email.send_keys("test@test.com")

attach_button = browser.find_element(By.ID, "file")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
attach_button.send_keys(file_path)

submit_button = browser.find_element(By.TAG_NAME, "button")
submit_button.click()
