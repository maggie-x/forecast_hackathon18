
from flask import *
import json
import sys
import os

app = Flask(__name__)


def testPrintCourses():
    courses = ["MATH1131", "MATH1231", "COMP1531", "COMP1521"]
    return render_template('index.html', courses = courses)