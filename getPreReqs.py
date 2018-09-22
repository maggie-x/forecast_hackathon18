from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
from Course import *

def remove_html_tags(text):
    """Remove html tags from a string"""

    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = clean.replace("\n", '')
    return clean

def removePrereqText(text):
    matched = re.match('Prerequisite: (.*)',text)
    if(matched):
        return matched.group(1)
    else:
        return None

courses = ["COMP3121", "COMP2521", "COMP2511"]

parsedCourses = []

for course in courses:
    url = "https://www.handbook.unsw.edu.au/undergraduate/courses/2019/{}".format(course)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    data = []

    # find prereqs
    # data = soup.find("readMoreSubjectConditions", "a-card-text m-toggle-text")
    data = soup.find_all("div", "a-card-text m-toggle-text has-focus")
    # print(data[1]) # hard-coding, prereq always herE?
    prereqs_string = remove_html_tags(str(data[1]))

    # element_string = removePrereqText(element_string)

    curr = Course(course, prereqs_string, )
    parsedCourses.append(curr)



    # find available terms


    # curr = Course()

'''
<div class="a-card m-bottom-2" id="SubjectConditions">
      <h3 tabindex="0" data-hbui="readmore__heading">
        Conditions for Enrolment
      </h3>
      <div data-hbui="readmore" tabindex="0" id="readMoreSubjectConditions" class="m-read-more-toggle no-truncate">
        <div data-hbui="readmore__toggle-text" class="a-card-text m-toggle-text has-focus">
          <div>Prerequisite: COMP1927 or COMP2521</div>
        </div>
        <div class="a-card-footer m-read-more-footer">
          <a data-hbui="readmore__toggler" role="button" tabindex="-1" aria-hidden="true" class="m-read-more toggler" href="#">
            Read More <span>Conditions for Enrolment</span>
          </a>
          <a data-hbui="readmore__toggler" role="button" tabindex="-1" aria-hidden="true" class="m-show-less toggler" href="#">
            Read Less <span>Conditions for Enrolment</span>
          </a>
        </div>
      </div>
    </div>
'''
