"""
Data keeping count of comment count for the running of this course in the 2013-2014 academic year. (The first time it ran).

I mainly record the negative comments here.
"""
from analyse import plot

Comments = {
            "'You should probably write that down'": 2,
            "Board is messy": 8,
            "Candy of low standard ('bring fruit')": 4,
            "Clarify which Chapter we are doing in class": 3,
            "Examples/Games unhelpful": 3,
            "Game Theory v Queueing Theory": 1,
            "I do not trust my classmates": 1,
            "I don't want to Volunteer / Picker is stressful": 5,
            "I would like to write more in lectures": 1,
            "Lack of detail / Doesn't go through proofs": 5,
            "More examples": 4,
            "More time on theory": 2,
            "No time for B.S.": 1,
            "Notification of when notes change": 4,
            "Spending a lot of time outside of lecture on this module": 1,
            "Too fast in lectures": 11,
            "Too many mistakes": 4,
            "Too many sources of content (blogs, videos, notes etc...)": 1,
            "Too much content": 1,
            "Want exam style examples": 9,
            "Would prefer to write more notes as opposed to online as it's easy to miss lectures": 1,
            "von Neumann, Zero-sum games...": 1,
           }

plot(Comments, '2013-2014.pdf')
