#!/usr/bin/env python
from sys import argv
from os import system

e = argv[1][:-3]
print e

system("sed -i '' 's/.md/.html/g' %s" % (e + ".md"))
system("pandoc -s " + e + ".md -N -o " + e + ".html --mathjax")
system("sed -i '' 's/.html/.docx/g' %s" % (e + ".md"))
system("pandoc " + e + ".md -o " + e + ".docx")
system("sed -i '' 's/.docx/.pdf/g' %s" % (e + ".md"))
system("pandoc " + e + ".md -N -o " + e + ".pdf --latex-engine=xelatex")
system("sed -i '' 's/.pdf/.md/g' %s" % (e + ".md"))
