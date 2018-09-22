from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
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

# courses = ["COMP3121", "COMP2521", "COMP2511"]
# parsedCourses = []
def courseFunc(courseName):
    page = "https://www.handbook.unsw.edu.au/undergraduate/courses/2019/"
    page = page+courseName
    return page
    #can also use re.search()
def check_course(text):
    matched = re.match('([A-Z]{4}[0-9]{4})',text)
    if(matched):
        return matched.group(0)
    else:
        return None
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




def parsePreReqs(course):
    url = courseFunc(course)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    data = []

    # find prereqs
    # data = soup.find("readMoreSubjectConditions", "a-card-text m-toggle-text")
    data = soup.find_all("div", "a-card-text m-toggle-text has-focus")
    prereqs_string = ""
    if(len(data)>1):
      prereqs_string = remove_html_tags(str(data[1]))

    # element_string = removePrereqText(element_string)
    # print(curr.availableTerms)
    return prereqs_string

def getCourseInfo(course):
  prereqs = parsePreReqs(course)
  offerings = getOfferings(course) # offerings = (True,False,False, False) tuple
  curr = Course(course, prereqs, offerings)
  return curr

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
