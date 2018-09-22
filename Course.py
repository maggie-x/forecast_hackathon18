import sys
import os

class Course:

    def __init__(self, name,prereqs, offerings): # availableTerms (0,1,1), meaning offered in t2 and t3
        self.name = name
        self.prereqs = prereqs
        self.offerings = offerings

    def getName(self):
        return self.name
    def getPreReqs(self):
        return self.prereqs
    def getOfferings(self):
        return self.offerings

    def setPreReqs(self, prereqs):
        self.prereqs = prereqs

    def setAvailable(self, availableTerms):
        self.availableTerms = availableTerms

    def setChoice(self):
        self.chosen = True

