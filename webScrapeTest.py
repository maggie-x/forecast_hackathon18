from urllib.request import urlopen
from bs4 import BeautifulSoup
page = urlopen("https://www.handbook.unsw.edu.au/undergraduate/specialisations/2019/COMPA1")
soup = BeautifulSoup(page, 'html.parser')
data = []
data = soup.find_all("div", "m-single-course-top-row")
print(data)