graph = [(2,1),(3,2),(4,3),(6,4),(1,6),(3,1),(6,3),(2,6),(4,2),(5,4),(1,5)]

l_graph = len(graph)
i = 0
node_list = []
node_dict = {}

while i < l_graph:
	j = 0
	while j < 2:
		node_list.append(graph[i][j])
		j += 1
	i +=1
node_list = set(node_list)
node_list = list(node_list)
print(node_list)
# finds unique nodes

for item in node_list:
	i = 0
	deg_counter = 0
	while i < l_graph:
		if graph[i][0] == node_list[item-1]:
			deg_counter += 1
		elif graph[i][1] == node_list[item-1]:
			deg_counter += 1
		i += 1
	print("Degree of node ", node_list[item-1], " is ", deg_counter)

	name = "node_" + str(node_list[item-1])
	node_dict[name] = deg_counter

print(node_dict)