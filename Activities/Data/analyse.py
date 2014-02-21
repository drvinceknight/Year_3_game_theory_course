"""Analyse any data file from activities in this class

Usage:
    analyse.py <file>

"""
from __future__ import division
from csv import reader
import matplotlib.pyplot as plt

class BestResponsesToMixedStrategies():
    """
    A class for an instance of best responses to mixed strategies data which must be of the form:
    Name,R1,R2,R3
    Vince,HHHHHH,TTTTTT,THTHTH
    """
    class Player():
        def __init__(self,row):
            self.name = row[0]
            if self.name == '':
                self.name = 'Anonymous'
            self.strategies = {'R1': list(row[1]),
                               'R2': list(row[2]),
                               'R3': list(row[3])}

            self.score = {'R1':0, 'R2':0, 'R3':0}

    def __init__(self, f):
        self.data = [self.Player(row) for row in reader(open(f, 'r'))]
        self.computer1 = list(raw_input('Write PC round 1 strategies (eg HHTTHT): '))
        self.computer2 = list(raw_input('Write PC round 2 strategies (eg HHTTHT): '))
        self.computer3 = list(raw_input('Write PC round 3 strategies (eg HHTTHT): '))

    def analyse(self):
        # Analysing mixed strategies
        self.strategies = {'R1':0, 'R2':0, 'R3':0}
        k = 0
        for p in self.data:
            for pair in zip(self.computer1,p.strategies['R1']):
                k += 1
                if pair[1] == 'H':
                    self.strategies['R1'] += 1
                    if pair[0] == 'H':
                        p.score['R1'] += -2
                    else:
                        p.score['R1'] += 1
                else:
                    if pair[0] == 'H':
                        p.score['R1'] += 2
                    else:
                        p.score['R1'] += -1
            for pair in zip(self.computer2,p.strategies['R2']):
                if pair[1] == 'H':
                    self.strategies['R2'] += 1
                    if pair[0] == 'H':
                        p.score['R2'] += -2
                    else:
                        p.score['R2'] += 1
                else:
                    if pair[0] == 'H':
                        p.score['R2'] += 2
                    else:
                        p.score['R2'] += -1
            for pair in zip(self.computer3,p.strategies['R3']):
                if pair[1] == 'H':
                    self.strategies['R3'] += 1
                    if pair[0] == 'H':
                        p.score['R3'] += -2
                    else:
                        p.score['R3'] += 1
                else:
                    if pair[0] == 'H':
                        p.score['R3'] += 2
                    else:
                        p.score['R3'] += -1
        for rnd in self.strategies:
            self.strategies[rnd] /= k

            x = self.strategies[rnd]
            ind = [1,2]
            width = .5
            fig, ax = plt.subplots()
            cax = ax.bar(ind,[x, 1-x], width)
            ax.set_xticks([i + width / 2 for i in ind])
            ax.set_xticklabels(['$x$','$1-x$'])

            x1,x2,y1,y2 = plt.axis()
            plt.axis((x1,x2,0,1))

            plt.title('Mixed strategy for %s' % rnd)

            plt.savefig('%sstrategiesvbestresponse.png' % rnd)
        self.winner = {'R1':0, 'R2':0, 'R3':0}
        for rnd in self.winner:
            self.winner[rnd] = [p for p in self.data if p.score[rnd] == max(p.score[rnd] for p in self.data)]


    def show(self):
        print self.strategies
        for rnd in self.winner:
            print "%s: %s winners" % (rnd, len(self.winner[rnd]))
            for p in self.winner[rnd]:
                print '\t',p.name
                print '\t',p.score[rnd]
                print '\t',p.strategies[rnd]
            print "Mean score: %s" % (sum([p.score[rnd] for p in self.data]) / len(self.data))
            plt.figure()
            plt.hist([p.score[rnd] for p in self.data])
            plt.title('Score for %s' % rnd)
            plt.savefig('%sscore.png' % rnd)
            positiveplayers = [p for p in self.data if p.score[rnd] > 0]
            x = [s for p in positiveplayers for s in p.strategies[rnd]].count('H') / len([s for p in positiveplayers for s in p.strategies[rnd]])
            print "%s had a positive score playing sigma_2 = (%s, %s)" % (len(positiveplayers), x, 1-x)
            zeroplayers = [p for p in self.data if p.score[rnd] == 0]
            if len(zeroplayers) > 0:
                x = [s for p in zeroplayers for s in p.strategies[rnd]].count('H') / len([s for p in zeroplayers for s in p.strategies[rnd]])
                print "%s had a zero score playing sigma_2 = (%s, %s)" % (len(zeroplayers), x, 1-x)
            else:
                print "%s had a zero score" % (len(zeroplayers))
            negativeplayers = [p for p in self.data if p.score[rnd] < 0]
            x = [s for p in negativeplayers for s in p.strategies[rnd]].count('H') / len([s for p in negativeplayers for s in p.strategies[rnd]])
            print "%s had a negative score playing sigma_2 = (%s, %s)" % (len(negativeplayers), x, 1-x)
        overallwinners = [p for p in self.data if sum([p.score[rnd] for rnd in p.score]) == max([sum([p.score[rnd] for rnd in p.score]) for p in self.data])]
        print "Overall winners: %s with score: %s" % ([p.name for p in overallwinners],max([sum([p.score[rnd] for rnd in p.score]) for p in self.data]) )
        for p in overallwinners:
            print p.name
            for rnd in p.strategies:
                print '\tR1: %s' % p.strategies[rnd]

        plt.figure()
        plt.hist([sum([p.score[rnd] for rnd in p.score]) for p in self.data])
        plt.title('Cumulative score')
        plt.savefig('cumulativescore.png')




class MatchingPennies():
    """
    A class for an instance of matching pennies data which must be of the form:
    Game1Row, Game1Col, Game2Row, Game2Col
    T,T,H,T
    """
    def __init__(self, f):
        self.data = [row for row in reader(open(f, 'r'))]
    def show(self):
        print self.dictionaries
        print self.mixedstrategiesgame2[-1]
    def analyse(self):
        self.dictionaries = [{'H':0, 'T':0}, {'H':0, 'T':0}, {'H':0, 'T':0}, {'H':0, 'T':0}]
        self.mixedstrategiesgame1 = [[0,0]]
        self.mixedstrategiesgame2 = [[0,0]]

        self.scoresgame1 = [[0,0]]
        self.scoresgame2 = [[0,0]]

        for row in self.data[1:]:
            for d in range(len(self.dictionaries)):
                self.dictionaries[d][row[d]] += 1
            self.mixedstrategiesgame1.append([self.mixedstrategiesgame1[-1][0] + int(row[0] == 'H'), self.mixedstrategiesgame1[-1][1] + int(row[1] == 'H')])
            self.mixedstrategiesgame2.append([self.mixedstrategiesgame2[-1][0] + int(row[2] == 'H'), self.mixedstrategiesgame2[-1][1] + int(row[3] == 'H')])
            if row[0] == row[1]:
                self.scoresgame1.append([self.scoresgame1[-1][0] + 1, self.scoresgame1[-1][1] - 1])
            else:
                self.scoresgame1.append([self.scoresgame1[-1][0] - 1, self.scoresgame1[-1][1] + 1])

            if row[2] == row[3]:
                self.scoresgame2.append([self.scoresgame2[-1][0] + int(row[2] == 'H') + 1, self.scoresgame2[-1][1] - (1 + int(row[2] == 'H'))])
            else:
                self.scoresgame2.append([self.scoresgame2[-1][0] - int(row[2] == 'H') - 1 , self.scoresgame2[-1][1] + (1 + int(row[2] == 'H'))])

        self.nbrofgames = len(self.mixedstrategiesgame1)
        for k in range(1, self.nbrofgames + 1):
            self.mixedstrategiesgame1[k - 1] = [i/k for i in self.mixedstrategiesgame1[k - 1]]
            self.mixedstrategiesgame2[k - 1] = [i/k for i in self.mixedstrategiesgame2[k - 1]]
            self.scoresgame1[k - 1] = [i/k for i in self.scoresgame1[k - 1]]
            self.scoresgame2[k - 1] = [i/k for i in self.scoresgame2[k - 1]]

        plt.figure()
        x = range(1, self.nbrofgames + 1)
        y = [i[0] for i in self.scoresgame1]
        plt.plot(x,y, label="Player 1: Mean score")
        y = [i[1] for i in self.scoresgame1]
        plt.plot(x,y, label="Player 2: Mean score", color='red')
        plt.legend(loc=4)
        plt.savefig('meanscroresgame1.png')

        plt.figure()
        x = range(1, self.nbrofgames + 1)
        y = [i[0] for i in self.scoresgame2]
        plt.plot(x,y, label="Player 1: Mean score")
        y = [i[1] for i in self.scoresgame2]
        plt.plot(x,y, label="Player 2: Mean score", color='red')
        plt.legend(loc=4)
        plt.savefig('meanscroresgame2.png')

        plt.figure()
        x = range(1, self.nbrofgames + 1)
        y = [i[0] for i in self.mixedstrategiesgame1]
        plt.plot(x,y, label="Player 1: Probability of playing 'H'")
        x = range(1, self.nbrofgames + 1)
        y = [i[1] for i in self.mixedstrategiesgame1]
        plt.plot(x,y, label="Player 2: Probability of playing 'H'", color='red')
        y = [.5 for i in self.mixedstrategiesgame1]
        plt.plot(x, y, 'g--')
        plt.legend(loc=4)
        plt.savefig('mixedstrategiesgame1.png')

        plt.figure()
        x = range(1, self.nbrofgames + 1)
        y = [i[0] for i in self.mixedstrategiesgame2]
        plt.plot(x,y, label="Player 1: Probability of playing 'H'")
        x = range(1, self.nbrofgames + 1)
        y = [i[1] for i in self.mixedstrategiesgame2]
        plt.plot(x,y, label="Player 2: Probability of playing 'H'", color='red')
        y = [1/3 for i in self.mixedstrategiesgame1]
        plt.plot(x, y, 'c--')
        y = [1/2 for i in self.mixedstrategiesgame1]
        plt.plot(x, y, 'm--')
        plt.legend(loc=4)
        plt.savefig('mixedstrategiesgame2.png')





if __name__ == '__main__':
    from docopt import docopt
    arguments = docopt(__doc__, version='1.0')

    classes = {'matchingpennies': MatchingPennies,
               'bestresponsemixedstrategies': BestResponsesToMixedStrategies}

    def returnclass(filename):
        for key in classes:
            if key in filename:
                return classes[key](filename)

    a = returnclass(arguments['<file>'])
    a.analyse()
    a.show()
