"""Analyse any data file from activities in this class

Usage:
    analyse.py <file>

"""
from csv import reader
import matplotlib.pyplot as plt


class MatchingPennies():
    """
    A class for an instance of matching pennies data which must be of the form:
    Game1Row, Game1Col, Game2Row, Game2Col
    T,T,H,T
    """
    def __init__(self, f):
        self.data = [row for row in reader(open(f, 'r'))]
    def analyse(self):
        self.dictionaries = [{'H':0, 'T':0}, {'H':0, 'T':0}, {'H':0, 'T':0}, {'H':0, 'T':0}]
        for row in self.data[1:]:
            for d in range(len(self.dictionaries)):
                self.dictionaries[d][row[d]] += 1





if __name__ == '__main__':
    from docopt import docopt
    arguments = docopt(__doc__, version='1.0')

    classes = {'matchingpennies': MatchingPennies}

    def returnclass(filename):
        for key in classes:
            if key in filename:
                return classes[key](filename)

    a = returnclass(arguments['<file>'])
    a.analyse()
    print a.dictionaries
