# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
	i = n
	# set incriment to input number
	while i > 0:
	# only run while greater than 0
		i = i-1
		# decrease incriment by one each loop
		n = n + i
		# add incriment to input
	total = n + 2
	# add minimum value to 2
	return total

def clique(n):
	print "in a clique..."
	for j in range(n):
		for i in range(j):
			print i, "is friends with", j
