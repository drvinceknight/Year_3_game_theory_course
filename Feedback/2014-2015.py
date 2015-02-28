"""
Data keeping count of comment count for the running of this course in the 2014-2015 academic year.

I mainly record the negative comments here.
"""
from analyse import plot

Comments = {
           "Website - Good": 44,
           "Active learning": 52,
           "More info on exam, more steps in explanation": 11,
           "Good explanations": 7,
           "Vince helpful/approachable": 15,
           "Assessed coursework perhaps?": 4,
           "In class games take too long": 10,
           "Thanks for printing (sorry about puppy)": 8,
           "What is up with the stapling!!!": 9,
           "Poor handwriting/disorganised board": 7,
           "Videos - Good": 4,
           "Name picker is terrifying": 1,
           "Long pauses - awkward ('perhaps wait ten seconds')": 13,
           "Waiting to start wastes time": 2,
           "A lot of examples": 7,
           "More time should be spent on the handouts as they are currently being printed out for no reason": 1,
           "S, s and s_i is confusing": 2,
           "More in depth videos please": 1,
           "Quite hard to take notes in lecture": 1,
           "Love the BS lectures": 2,
           "Too much chocolate": 1,
           "Reason I get out of bed in the morning": 1,
           "Please make the revision lectures useful! Don't waste them.": 3,
           "Pace - Good": 2,
           "Keep in line with content, ie no irrelevant rugby info": 1,
           "Not good for lactose intolerant people": 1,
           "Homework system": 7,
           "Vince is  bit scary": 1,
           "More examples": 1,
           "Skeleton notes would be nice": 1,
           "Not good for lazy people who won't read notes in spare time": 1,
           "Communication between lectures is good (YAY)": 1,
           "Lecturer's view that lectures are pointless contradicts the way he teaches the module": 1,
           "Be more assertive when starting the lecture, those who are quiet also have to wait": 1,
           }

plot(Comments, '2014-2015.pdf')
