#!/usr/bin/env python
from sys import argv
from os import system

mediaserver = "http:\/\/drvinceknight.github.io\/Year\_3\_game\_theory\_course\/Homework\/"

e = argv[1][:-3]
print e

# HTML
system("sed 's/.md/.html/g' %s > tmp" % (e + ".md"))
system("sed 's/\!\[.*\]/\!\[\]/g' tmp > tmp1")  # Get rid of captions
system("sed 's/](/](%s/g' tmp1 > tmp" % mediaserver)  # Change media server to github
string = "\n\n(Other versions of the above: [pdf](%s%s) [docx (not recommended)](%s%s))" % (mediaserver, e+".pdf", mediaserver, e+".docx")
system("echo '%s' >> tmp" % string)
system("pandoc -s tmp -N -o " + e + ".html --mathjax")
#system("sed 's/.md/.docx/g' %s > tmp" % (e + ".md"))
#system("pandoc tmp -o " + e + ".docx")

# PDF
system("sed 's/.md/.pdf/g' %s > tmp" % (e + ".md"))
system("pandoc tmp -N -o " + e + ".pdf --latex-engine=xelatex")
system("rm tmp")
system("rm tmp1")
