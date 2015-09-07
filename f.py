__author__ = 'kud'
class Fib(object):
    def __init__(self, number):
        self.number = number
        self.__fib1 = 1
        self._fib2 = 1

    def fibo(self):
        i = 0
        while i < self.number:
            fib_sum = self._fib2 + self.__fib1
            self.__fib1 = self._fib2
            self._fib2 = fib_sum
            i += 1
            print fib_sum

y = Fib(10)
y.fibo()