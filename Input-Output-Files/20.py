__author__ = 'kud'

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Whole file:\n"
print_all(current_file)

print "Rewind a file.\n"
rewind(current_file)
'''
print "Print 3 lines:\n"
current_line=1
for line in current_file:
    print current_line, line
    current_line=current_line+1
    if current_line == 4:
        break
'''

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line +=  1
print_a_line(current_line, current_file)