__author__ = 'kud'
from sys import argv
from os.path import exists
import shutil

script, file_from, file_to = argv

shutil.copyfile(file_from, file_to)

"""
print "Copying file %s to %s" %(file_from,file_to)

input = open(file_from)
indata = input.read()

print "This file is %d bytes." %len(indata)

print "Does the output file exists? %r" %exists(file_to)
print "Ready, press RETURN to continue, CTRL+C to abort."
raw_input()

output = open(file_to, "w")
output.write(indata)

print "All done."

output.close()
input.close()
"""
