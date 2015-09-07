__author__ = 'kud'
print "Let's practice everything."
print "You \'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\t This is the poem
and here is \n a new line
\n\t\t new line and two tabs.
"""

print "----------"
print poem
print "----------"

five = 10-2+3-6
print "This is five: %d" %five

def formula(starter):
    beans = starter*500
    jars = beans/1000
    crates = jars/100
    return beans,jars,crates

start = 10000
beans,jars,crates = formula(start)

print "with start point: %d" %start
print "We'd have %d beans, %d jars, %d crates." %(beans,jars,crates)

start = start/10
print "We can do it another way:"
print  "We'd have %d beans, %d jars, %d crates." %formula(start)