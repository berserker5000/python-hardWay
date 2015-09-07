__author__ = 'kud'
count = [1,2,3,4,5,6]
fruits = ['apples', ' oranges', 'pears', 'apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in count:
    print "This is the count: %d" %number

for fruit in fruits:
    print "A fruit of type: %s" %fruit

for i in change:
    print "I got %r" %i

elements = []

for i in range(0,9):
    print "adding %d to list." %i
    elements.append(i)

for i in elements:
    print "Element was: %d" %i