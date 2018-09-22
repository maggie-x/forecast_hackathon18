from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
def remove_html_tags(text):
    """Remove html tags from a string"""
    
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
    
page = urlopen("https://www.handbook.unsw.edu.au/undergraduate/specialisations/2019/COMPA1")
soup = BeautifulSoup(page, 'html.parser')
data = []
data = soup.find_all("div", "m-single-course-top-row")
data_string = str(data[0])
data_string = remove_html_tags(data_string)


