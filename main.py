from flask import Flask, app, render_template, url_for, redirect, session, request
from flask_bootstrap import Bootstrap
import json
import sys
import os
from webScrapeTest import *
from getCourseInfo import *

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def testPrintCourses():
    firstYearCourses = course_scraper()
    courseObjects = []
    for course in firstYearCourses:
        courseObjects.append(getCourseInfo(course))


    # group via offerings
    summer = []
    t1 = []
    t2 = []
    t3 = []
    for cObject in courseObjects:
        if cObject.availableTerms[0] == True:
            summer.append(cObject)
        if cObject.availableTerms[1] == True:
            t1.append(cObject)
        if cObject.availableTerms[2] == True:
            t2.append(cObject)
        if cObject.availableTerms[3] == True:
            t3.append(cObject)

    # list of courses per term
    # offering [[summer][t1][t2][t3]]
    return render_template('index.html', courseObjects = courseObjects, summer=summer, t1=t1, t2=t2, t3=t3)


if __name__ == '__main__':
	app.run(debug=True, port=5001)