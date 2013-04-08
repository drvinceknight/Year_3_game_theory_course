#!/usr/bin/env python
from sys import argv
from os import system

e = argv[1][:-3]
print e

system("sed 's/.md/.html/g' %s > tmp" % (e + ".md"))
system("pandoc -s tmp -N -o " + e + ".html --mathjax")
system("sed 's/.md/.docx/g' %s > tmp" % (e + ".md"))
system("pandoc tmp -o " + e + ".docx")
system("sed 's/.md/.pdf/g' %s > tmp" % (e + ".md"))
system("pandoc tmp -N -o " + e + ".pdf --latex-engine=xelatex")
system("rm tmp")
