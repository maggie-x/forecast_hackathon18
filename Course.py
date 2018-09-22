import sys
import os

class Course:

    def __init__(self, name): # availableTerms (0,1,1), meaning offered in t2 and t3
        self.name = name

    def getName(self):
        return self.__name__

    def setPreReqs(self, prereqs):
        self.prereqs = prereqs

    def setAvailable(self, availableTerms):
        self.availableTerms = availableTerms

    def setChoice(self):
        self.chosen = True

