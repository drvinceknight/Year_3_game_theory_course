#!/usr/bin/env python
from sys import argv
from os import system

e = argv[1][:-3]

system("pandoc " + e + ".md -o " + e + ".pdf --latex-engine=xelatex")
system("pandoc " + e + ".md -o " + e + ".html --webtex")
system("pandoc " + e + ".md -o " + e + ".docx")
