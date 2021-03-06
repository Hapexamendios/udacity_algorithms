import math

def time(n):
    """ Return the number of steps 
    necessary to calculate
    `print countdown(n)`"""
    steps = 0
    steps = (n/5) * 2 + 3
    return steps

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print(y)

#print countdown(50)

def example(m):
    steps = 3 + ((m // 5) *2) + (2 * (1 % ((m % 5)+1)))
    print(steps)
    # this is essentially a strange way to round up

    '''
    3 + 2 * math.ceil(n/5.0)
    ceil function rounds up to nearest int
    and is thus the solution
    '''

example(0)