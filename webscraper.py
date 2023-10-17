from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.bu.edu/academics/cas/courses/cas-cs-101/'
browser = webdriver.Chrome()
browser.get(url) 
element = browser.find_element(By.CLASS_NAME,'cf-hub-offerings')
print(element.text)
