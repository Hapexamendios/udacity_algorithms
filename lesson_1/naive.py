def naive(a, b):
    x = a
    y = b
    z = 0
	# start with z = 0
    while x > 0:
	# run, if a is 1 or more
        z = z + y
        # each loop, add b to z
        x = x - 1
        # each loop, subtract one from a
    return z
print(naive(5,5))