__author__ = 'rpercy'

def fib(n):
    return reduce(lambda x,y: (x[1], x[0]+x[1]), range(n), (0,1))[0]

print fib(0)
print fib(1)
print fib(2)
print fib(10)
print fib(100)
