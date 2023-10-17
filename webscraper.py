from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

startPage = 'https://www.bu.edu/academics/cas/courses/'
browser = webdriver.Chrome()
browser.get(startPage)
linkNum = 1
courseList = {}
while True:
    try:
        url = browser.find_element(By.XPATH,f'//*[@id="post-6984"]/ul/li[{linkNum}]/a').get_attribute('href')
        browser.get(url)
        course = {}
        try:
            hubList = browser.find_element(By.CLASS_NAME,'cf-hub-offerings')
            course["hub"] = hubList.text
        except NoSuchElementException:
            pass
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
        course["fall"] = fallSections
        course["spring"] = springSections
        courseName = browser.find_element(By.XPATH,'//*[@id="col1"]/div/h2').text
        courseList[courseName] = course
        browser.get(startPage)
        linkNum += 1
    except NoSuchElementException:
        break