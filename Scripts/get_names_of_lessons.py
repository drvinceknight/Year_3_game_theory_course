#! /usr/bin/env python

import sys
import os

if len(sys.argv) == 1:
    target_dir = "../Lesson_Plans"
else:
    target_dir = sys.argv[1]

list_of_plans = os.listdir(target_dir)
list_of_plans = [p for p in list_of_plans if p != "makefile"]
number_of_plans = len(list_of_plans)
print number_of_plans


index_file = open("../index.md", "w")
index_file.write("# OR3 - Game Theory")
index_file.write("\n## Lesson plans")
index_file.write("\n")

for i in range(len(list_of_plans)):
    outfile = open(target_dir + "/" + list_of_plans[i])
    data = outfile.read().split("\n")
    outfile.close()

    index_file.write("\n%s. Lecture %s: [%s](./Lesson_Plans/Lesson_%.02d.md)" % (i + 1, i + 1, data[1][2:], i + 1))

index_file.close()
