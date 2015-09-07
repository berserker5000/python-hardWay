__author__ = 'kud'
def inc(n,k):
    i =0
    number =[]

    while i<n:
        print "At top i is %d" %i
        number.append(i)

        i+=k
        print "Number now: ", number
        print "At the bottom i is %d" %i

    print "The numbers: "

    for num in number:
        print num

less = int(raw_input("Input the number: "))
increment = int(raw_input("Increment number: "))
#inc(less,increment)

def inc1(n,k):
    i=0
    numbers=[]
    for i in range(0,n,k):
        print "Number on the top is %d" %i
        numbers.append(i)
        print "Numbers are: ", numbers

    for num in numbers:
        print num

inc1(less,increment)