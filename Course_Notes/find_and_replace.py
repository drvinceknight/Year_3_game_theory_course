#!/usr/bin/env python
from sys import argv
from os import system, listdir

md_files = [f for f in listdir("./") if f[-3:] == ".md"]

for e in md_files:
    e = e[:-3]
    print e

    system("sed -i '' 's/.pdf/.md/g' %s" % (e + ".md"))
