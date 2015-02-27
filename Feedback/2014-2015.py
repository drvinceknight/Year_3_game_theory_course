"""
Data keeping count of comment count for the running of this course in the 2014-2015 academic year.

I mainly record the negative comments here.
"""
from analyse import plot

Comments = {
            "comments": count,
           }

plot(Comments, '2014-2015.pdf')
