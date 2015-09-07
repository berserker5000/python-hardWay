__author__ = 'kud'
class Thing(object):
    def test(self,hi):
        self.hi = hi
        return self.hi

a = Thing()
print a.test("hello")

stuff = ['saf0','sdf','ih3hono']
print stuff.pop()
print(stuff)