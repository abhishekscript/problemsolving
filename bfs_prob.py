from queue import Queue

adj_list = {
	"A" : ["B", "D"],
	"B" : ["A", "C"],
	"C" : ["B"],
	"D" : ["A", "E", "F"],
	"E" : ["D", "F", "G"],
	"F" : ["D", "E", "H"],
	"G" : ["E", "H"],
	"H" : ["G", "F"]
}


sourceNode = "A"

level   = {}
parent  = {}
visited = {}


for node in adj_list:
	level[node] = 0
	parent[node] = None
	visited[node] = False

visited[sourceNode] = True

queue = Queue()
queue.put(sourceNode)
while not queue.empty():

	current_node = queue.get()
	print("Parent   :", current_node)
	print("Children : ")
	for node in adj_list[ current_node ]:
		if not visited[node]:
			visited[node] = True
			parent[node] = current_node
			level[node]  = level[current_node]+1
			queue.put(node)
			print("\t\t",node)
