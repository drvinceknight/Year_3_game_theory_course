from glob import glob
from subprocess import call

mdf = glob('./*.md')
for f in mdf:
    call(['./pandocipy_given_file.py', f])
