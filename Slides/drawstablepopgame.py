"""
Script to write tikz code to draw population dynamics
"""
from __future__ import division
from random import random, choice

epsilon = .5
rows = 10
columns = 20

tikzcode = ""

for m in range(columns):
    for n in range(rows):
        if random() < epsilon:
            string = "\only<1-2>{\\node at (%s, %s) [fill, color=red] {};}\n" % (m, n)
            string += "\only<2-3>{\\node at (%s, %s) [fill, color=blue] {};}\n" % (m, n)
        else:
            string = "\only<1-2>{\\node at (%s, %s) [fill, color=red] {};}\n" % (m, n)
            string += "\only<3>{\\node at (%s, %s) [fill, color=blue] {};}\n" % (m, n)
        tikzcode += string

epsilon = .1

for m in range(columns):
    for n in range(rows):
        if random() < epsilon:
            life = choice([6,7,8])
            string = "\only<4,%s->{\\node at (%s, %s) [fill, color=red] {};}\n" % (life, m, n)
            string += "\only<5-%s>{\\node at (%s, %s) [fill, color=blue] {};}\n" % (life - 1, m, n)

        else:
            string += "\only<4->{\\node at (%s, %s) [fill, color=red] {};}\n" % (m, n)
        tikzcode += string

print tikzcode
