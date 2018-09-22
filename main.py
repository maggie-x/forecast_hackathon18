from flask import Flask, app, render_template, url_for, redirect, session, request
from flask_bootstrap import Bootstrap
import json
import sys
import os

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def testPrintCourses():
    courses = ["MATH1131", "MATH1231", "COMP1531", "COMP1521"] # should be list of course objects
    return render_template('index.html', courses = courses)


if __name__ == '__main__':
	app.run(debug=True, port=5001)