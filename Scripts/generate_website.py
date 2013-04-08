#! /usr/bin/env python

import os

# Open index file

index_file = open("../index.md", "w")
index_file.write("# Year 3 - Game Theory")
index_file.write("\n")

# Notes

index_file.write("""
This website is very much work in progress with content for the 3rd game theory course I'm teaching at Cardiff University.

The github repo for this course is [here](https://github.com/drvinceknight/Year_3_game_theory_course).

([My personal website](www.vincent-knight.com))
                 """)
index_file.write("\n")

# Write course notes

target_dir = "../Course_Notes"

list_of_chapters = os.listdir(target_dir)
list_of_md_chapters = [p for p in list_of_chapters if p[-3:] == ".md"]
number_of_chapters = len(list_of_md_chapters)
print "%s chapters read." % number_of_chapters

index_file.write("\n")
index_file.write("\n## Course Chapters")
index_file.write("\n")

for i in range(len(list_of_md_chapters)):
    outfile = open(target_dir + "/" + list_of_md_chapters[i])
    data = outfile.read().split("\n")
    outfile.close()
    file_name = list_of_md_chapters[i][:-3]
    index_file.write("\n%s. Chapter %s: %s" % (i + 1, i + 1, data[0][data[0].index("-") + 2:]))
    index_file.write("\n")
    index_file.write("\n\t[pdf(recommended)](./Course_Notes/%s.pdf), [html](./Course_Notes/%s.html), [docx](./Course_Notes/%s.docx)" % (file_name, file_name, file_name))
    index_file.write("\n")

# Write Lesson plans

target_dir = "../Lesson_Plans"
index_file.write("\n## Lesson plans")

list_of_plans = os.listdir(target_dir)
list_of_plans = [p for p in list_of_plans if p[-3:] == ".md"]
number_of_plans = len(list_of_plans)
print "%s lesson plans read." % number_of_plans

for i in range(len(list_of_plans)):
    outfile = open(target_dir + "/" + list_of_plans[i])
    data = outfile.read().split("\n")
    outfile.close()

    index_file.write("\n%s. Lecture %s: [%s](./Lesson_Plans/Lesson_%.02d.html)" % (i + 1, i + 1, data[1][2:], i + 1))

index_file.write("\n")

os.system("pandoc -s ../Notations_conventions.md -o ../Notations_conventions.html --mathjax")

index_file.write("""
## Some extra things:

- Here is a file containing a summary of the notations and conventions in this course: [html](./Notations_conventions.html).
- Here is a list of reading materials on game theory: [html](./Reading_list.html). I wrote a blog post describing some of the literature: [here](http://drvinceknight.blogspot.co.uk/2013/03/game-theory-reading-list.html).
- Here is a list of free and open source Game theory software: [here](http://drvinceknight.blogspot.co.uk/2013/03/open-source-andor-free-game-theory.html).
                 """)

# Add analytics tracking script

index_file.write("""
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-38016329-2']);
  _gaq.push(['_setDomainName', 'github.com']);
  _gaq.push(['_setAllowLinker', true]);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
                 """)


index_file.close()

os.system("pandoc ../index.md -o ../index.html")
