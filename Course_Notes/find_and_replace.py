#!/usr/bin/env python

import os

md_files = [e for e in os.listdir(".") if e[-3:] == ".md"]

for e in md_files:
    os.system("sed -i '' 's/.html/.pdf/g' %s" % e)

html_files = [e for e in os.listdir(".") if e[-5:] == ".html"]

for e in html_files:
    os.system("sed -i '' 's/.pdf/.html/g' %s" % e)
