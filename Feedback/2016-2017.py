"""
Data keeping count of comment count for the running of this course in the 2014-2015 academic year.

I mainly record the negative comments here.
"""
from analyse import plot

Comments = {
           "Website/resources - Good": 32,
           "Class activities - Good": 37,
           "Fun": 9,
           "Approachable": 8,
           "Coursework is vague": 7,
           "Like having coursework": 4,
           "Encourage to work outside of class - Good": 3,
           "Notation": 3,
           "Vegan chocolate/Percy pigs please": 3,
           "A little more help please": 3,
           "More time spent on notes in lectures": 2,
           "What's on the exam?": 2,
           "Not approachable": 2,
           "Name generator - bad": 1
           }

plot(Comments, '2016-2017.pdf')
