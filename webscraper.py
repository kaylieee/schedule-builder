from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

url = 'https://www.bu.edu/academics/cas/courses/cas-cs-101/'
browser = webdriver.Chrome()
browser.get(url) 
hubList = browser.find_element(By.CLASS_NAME,'cf-hub-offerings')
courseList = browser.find_element(By.CLASS_NAME,'cf-course')
# print(hubList.text)
tableNum = 1
fallSections = []
springSections = []
while True:
    try:
        semester = browser.find_element(By.XPATH,f'//*[@id="course-content"]/div[3]/h4[{tableNum}]')
        table = browser.find_element(By.XPATH,f'//*[@id="course-content"]/div[3]/table[{tableNum}]/tbody[1]/tr[2]')
        if semester.text[0] == 'F':
            fallSections.append(table.text)
        else:
            springSections.append(table.text)
        tableNum += 1
    except NoSuchElementException:
        break
print(fallSections)
print(springSections)




