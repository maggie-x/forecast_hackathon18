from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import os.path
def courseFunc(courseName):
    page = "https://www.handbook.unsw.edu.au/undergraduate/courses/2019/"
    page = page+courseName
    return page
#return as a list of courses
def remove_html_tags(text):
    """Remove html tags from a string"""

    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = clean.replace("\n", '')
    return clean
    #can also use re.search()
def check_course(text):
    matched = re.match('([A-Z]{4}[0-9]{4})',text)
    if(matched):
        return matched.group(0)
    else:
        return None
def course_scraper():
    page = urlopen("https://www.handbook.unsw.edu.au/undergraduate/specialisations/2019/COMPA1")
    soup = BeautifulSoup(page, 'html.parser')
    data = []
    data = soup.find_all("div", "m-single-course-top-row")
    data_string = []
    comp_courses = []
    # [A-Z]{4}[0-9]{4}
    for data_element in data:
        element_string = str(data_element)
        data_string.append(remove_html_tags(element_string))
    for element in data_string:
        comp_courses.append(check_course(element))
    return comp_courses
def term_scraper():
    page = urlopen("https://www.handbook.unsw.edu.au/undergraduate/courses/2019/COMP1511/")
    soup = BeautifulSoup(page, 'html.parser')
    data = []
    data = soup.find_all("div", "o-attributes-table-item")
    stringer =  remove_html_tags(str(data[3]))
    print(stringer)
    stringer = check_course2(stringer)
    #returns a tuple of available terms
def getOfferings(course):
    courseUrl = courseFunc(course)
    page = urlopen(courseUrl)
    soup = BeautifulSoup(page, 'html.parser')
    data = []
    data = soup.find_all("div", "o-attributes-table-item")
    stringer =  remove_html_tags(str(data[3]))
    stringer = check_course2(stringer)
    available = [False,False,False,False] #Order of Summer Term, Term 1, Term 2, Term 3
    if(re.search('Summer Term',stringer)):
        available[0] = True
    if(re.search('Term 1',stringer)):
        available[1] = True
    if(re.search('Term 2',stringer)):
        available[2] = True
    if(re.search('Term 3',stringer)):
        available[3] = True
    return available
def check_course2(text):
    matched = re.match('Offering Terms(.*)',text)
    if(matched):
        return matched.group(1)
    else:
        return None
