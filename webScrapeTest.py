from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import os.path
def course(courseName):
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

def course_scraper(): # gets all comp courses
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
    for element in comp_courses:
        if element != None:
            if not os.path.exists(element+'.csv'):
                with open(element+".csv","w") as f:
                    f.write(something)
    return comp_courses



