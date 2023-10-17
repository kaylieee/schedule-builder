from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

startPage = 'https://www.bu.edu/academics/cas/courses/'
browser = webdriver.Chrome()
browser.get(startPage)
courseList = {}
#get all class links on page
classes = browser.find_elements(By.XPATH,'//*[@id="post-6984"]/ul/li/a')
#convert all to url first to avoid stale element
urls = [c.get_attribute("href") for c in classes]
for url in urls:
    browser.get(url)
    courseTitle = browser.find_element(By.XPATH,'//*[@id="col1"]/div/h2').text
    course = {}
    #get hub reqs fulfilled if exists
    try:
        hubList = browser.find_element(By.CLASS_NAME,'cf-hub-offerings')
        course["hub"] = hubList.text
    except NoSuchElementException:
        pass
    tableNum = 1
    fallSections = []
    springSections = []
    #go through each table until one is not found, extracting information on each section
    while True:
        try:
            semester = browser.find_element(By.XPATH,f'//*[@id="course-content"]/div[3]/h4[{tableNum}]')
            table = browser.find_element(By.XPATH,f'//*[@id="course-content"]/div[3]/table[{tableNum}]/tbody[1]/tr[2]')
            #use first letter of title of each table to see if section is fall or spring
            if semester.text[0] == 'F':
                fallSections.append(table.text)
            else:
                springSections.append(table.text)
            tableNum += 1
        except NoSuchElementException:
            break
    course["fall"] = fallSections
    course["spring"] = springSections
    courseList[courseTitle] = course