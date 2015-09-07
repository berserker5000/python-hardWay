__author__ = 'kud'
def add(a,b):
    print "Adding %d + %d" %(a,b)
    return a+b

def subtract(a,b):
    print "Subtracting %d - %d" %(a,b)
    return a-b

def multiply(a,b):
    print "Multiplying %d * %d" %(a,b)
    return a*b

def devide(a,b):
    print "Deviding %d / %d" %(a,b)
    return a/b

a = add(30,5)
s = subtract(50, 26)
m = multiply(90, 65)
d = devide(50, 6)

print "a: %d, s: %d, m: %d, d: %d" %(a,s,m,d)

print "Here is a puzzle for you. w = add(a, subtract(s,multiply(s,devide(d,2))))"
w = add(a, subtract(s,multiply(s,devide(d,2))))
print "W is:", w
