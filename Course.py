import sys
import os

class Course:

    def __init__(self, name, prereqs, availableTerms): # availableTerms (0,1,1), meaning offered in t2 and t3
        self.name = name
        self.prereqs = prereqs
        self.availableTerms = availableTerms

    def getName(self):
        return self.__name__

    def setPreReqs(self, prereqs):
        self.prereqs = prereqs

    def setChoice(self):
        self.chosen = True
