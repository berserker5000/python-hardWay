__author__ = 'kud'
def c_and_c(c_c, b_o_c):
    print "You have %d cheeses" %c_c + "\nYou have %d boxes of crackers" %b_o_c + "\nMan, That's enough for a party! \nGet a blanket. \n"

print "We can just give the function numbers directly:"
c_and_c(20,30)

print "OR, we can use variables from our script:"
c_c = 10
b_o_c = 50
c_and_c(c_c,b_o_c)

print "We can even do math inside too:"
c_and_c(10+20,5+6)

print "And we can combine the two, variables and math:"
c_and_c(c_c+100, b_o_c+1000)