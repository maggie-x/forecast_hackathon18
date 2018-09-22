from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import CourseClass

def remove_html_tags(text):
    """Remove html tags from a string"""

    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = clean.replace("\n", '')
    return clean

courses = ["COMP3161", "COMP2521", "COMP2511"]

parsedCourses = []

for course in courses:
    url = "https://www.handbook.unsw.edu.au/undergraduate/specialisations/2019/{}/".format(course)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    data = []

    # find prereqs
    data = soup.find_all("id", "readMoreSubjectConditions")
    prereqs_string = []
    for dataElem in data:
        element_string = str(dataElem)
        print(element_string)
        prereqs_string.append(remove_html_tags(prereqs_string))


    # find available terms


    curr = CourseClass()

