"""
Script to write tikz code to draw population dynamics
"""
from __future__ import division
from random import random, choice

chi = .25
rows = 10
columns = 20
numbertillcomplete = 10

tikzcode = ""

for m in range(columns):
    for n in range(rows):
        c = 'green'
        if random() < chi:
            c = 'red'
            string = "\only<1>{\\node at (%s, %s) [fill, color=black] {};}\n" % (m, n)
            string += "\only<2->{\\node at (%s, %s) [fill, color=red] {};}\n" % (m, n)
        else:
            k = choice(range(2, numbertillcomplete))
            string = "\only<1>{\\node at (%s, %s) [fill, color=black] {};}\n" % (m, n)
            string += "\only<2-%s>{\\node at (%s, %s) [fill, color=green] {};}\n" % (k, m, n)
            string += "\only<%s->{\\node at (%s, %s) [fill, color=red] {};}\n" % (k + 1, m, n)
        tikzcode += string

print tikzcode
