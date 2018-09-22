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


    # courses = ["MATH1131", "MATH1231", "COMP1531", "COMP1521"] # should be list of course objects

    # list of courses per term
    # offering [[summer][t1][t2][t3]]
    return render_template('index.html', courseObjects = courseObjects, offerings = offerings)


if __name__ == '__main__':
	app.run(debug=True, port=5001)