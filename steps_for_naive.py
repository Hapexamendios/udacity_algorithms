# counting steps in naive as a function of a

def naive(a, b):
    x = a
    # step 1
    y = b
    # step 2
    z = 0
    #step 3
    while x > 0:
    # loop eval not counted
        z = z + y
        # once per loop
        x = x - 1
        # once per loop
    return z
    # return not counted

def time(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    steps = 0
    steps = 3 + a * 2
    return steps

print(time(10))