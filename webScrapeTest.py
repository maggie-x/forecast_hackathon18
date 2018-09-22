from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
def remove_html_tags(text):
    """Remove html tags from a string"""
    
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = clean.replace("\n", '')
    return clean
    #can also use re.search()
def check_course(text):
    matched = re.match('([A-Z]{4}[0-9]{4})',text)
    return matched.group(0)
page = urlopen("https://www.handbook.unsw.edu.au/undergraduate/specialisations/2019/COMPA1")
soup = BeautifulSoup(page, 'html.parser')
data = []
data = soup.find_all("div", "m-single-course-top-row")
data_string = []
# [A-Z]{4}[0-9]{4}
for data_element in data:
    element_string = str(data_element)
    data_string.append(remove_html_tags(element_string))
for element in data_string:
    print(check_course(element))

