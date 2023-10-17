from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def getHubList(browser):
    try:
        hubList = browser.find_element(By.CLASS_NAME,'cf-hub-offerings')
        return hubList.text
    except NoSuchElementException:
        return None

def getAllSections(browser):
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
    return fallSections, springSections

def getCourseInfo(browser):
    #get all info on one course
    course = {}
    course["hub"] = getHubList(browser)
    sections = getAllSections(browser)
    course["fall"] = sections[0]
    course["spring"] = sections[1]
    return course

startPage = 'https://www.bu.edu/academics/cas/courses/'
browser = webdriver.Chrome()
browser.get(startPage)
courseList = {}
#get all class links on page and convert to url
classes = browser.find_elements(By.XPATH,'//*[@id="post-6984"]/ul/li/a')
urls = [c.get_attribute("href") for c in classes]
for url in urls:
    browser.get(url)
    courseTitle = browser.find_element(By.XPATH,'//*[@id="col1"]/div/h2').text
    courseList[courseTitle] = getCourseInfo(browser)