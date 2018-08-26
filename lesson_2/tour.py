my_list = [1,5,9,12]
l = len(my_list)
def create_tour (nodes):
	tour_list = []
	# init my list

	i = 0
	# set incriment to zero

	length = len(nodes)
	# find length

	while i < length:

		#print(i)

		if i < length-1:
			tup = (nodes[i],nodes[i + 1])
		# if it's not the last node, tour is current node + next node

		elif i == length-1:
			tup = (nodes[i],nodes[0])
		# if it's the last node, tour is current node + first node
		
		#print(tup)

		i += 1
		# increment

		tour_list.append(tup)
		# append the list

		#print(tour_list)

	return

create_tour(my_list)
#print(l)
#first = my_list[0]
#print(first)