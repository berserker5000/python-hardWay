__author__ = 'kud'
class THeThign(object):

    def __init__(self):
        self.number = 0

    def some_func(self):
        print "I got called."

    def add_me(self, more):
        self.number +=more
        return self.number

a= THeThign()
b = THeThign()
a.some_func()
b.some_func()
print a.add_me(20)
print a.add_me(15)
print b.add_me(40)
print b.add_me(11)
print a.number
print b.number