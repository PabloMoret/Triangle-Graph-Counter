class Graph:
	def __init__(self, rowVertices, rowEdges, vertices, edges, amatrix):
		self.rowVertices = rowVertices
		self.rowEdges = rowEdges
		self.vertices = vertices
		self.edges = edges
		self.amatrix = amatrix

	def getVertices(graph):
		return " ".join(graph.rowVertices)

	def getEdges(graph):
		edge = ""
		for i in range(len(graph.vertices)):
			edge = edge + str(graph.rowEdges[i][0]) + str(graph.rowEdges[i][1]) + " "
		
		return edge

	def printAmatrix(graph):
		for i in range(len(graph.vertices)):
			print(graph.amatrix[i])


def countTriangles(graph):
	triangles = 0

	for row in range(len(graph.vertices)):
		for column in range(row, len(graph.vertices)):
			if graph.amatrix[row][column] == 1:
				for element in range(column+1, len(graph.vertices)):
					if graph.amatrix[row][element] == 1:
						if graph.amatrix[column][element] == 1:
							triangles += 1

	return triangles


def createGraph(path):
	vertices,edges = openFile(path)

	gv = vertices.split()
	ge = edges.split()

	graphVertices = []
	graphEdges = []

	graphRawVertices = []
	graphRawEdges = []

	for vertex in gv:
		graphVertices.append(vertex)
		graphRawVertices.append(vertex)

	for edge in ge:
		graphEdges.append((graphVertices.index(edge[0]),graphVertices.index(edge[1])))
		graphRawEdges.append((edge[0],edge[1]))

	for vertex in graphVertices:
		graphVertices[graphVertices.index(vertex)] = graphVertices.index(vertex)

	gvLen = len(graphVertices)

	graphAmatrix = [[0 for x in range(gvLen)] for y in range(gvLen)]

	for edge in graphEdges:
		graphAmatrix[edge[0]][edge[1]] = 1
		graphAmatrix[edge[1]][edge[0]] = 1

	return Graph(graphRawVertices, graphRawEdges, graphVertices, graphEdges,graphAmatrix)


def openFile(path):
	f = open(path, "r")

	fileVertices = f.readline().strip('\n')
	fileEdges = f.readline().strip('\n')

	f.close()

	return fileVertices,fileEdges


graph = createGraph("graph2.txt")

print("\nGiven the following graph G(V,E):\n")
print("V = {", graph.getVertices(), "}\n")
print("E = {", graph.getEdges(), "}\n")
print("And an adjacency matrix A = ")
graph.printAmatrix()
print("\nThe number of triangles in this graph is:", countTriangles(graph))
