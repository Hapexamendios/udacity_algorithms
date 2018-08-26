# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
	l_graph = len(graph)
	i = 0
	node_list = []
	while i < l_graph:
		j = 0
		while j < 2:
			node_list.append(graph[i][j])
			j += 1
		i +=1
	node_list = set(node_list)
	node_list = list(node_list)
	node_list.append(node_list[0])
	return node_list



graph = [(1,3),(3,7),(7,19),(19,25),(25,6),(6,1)]
l_graph = len(graph)
i = 0
node_list = []
while i < l_graph:
	j = 0
	while j < 2:
		node_list.append(graph[i][j])
		j += 1
	i +=1
node_list = set(node_list)
node_list = list(node_list)
node_list.append(node_list[0])
#print(node_list)