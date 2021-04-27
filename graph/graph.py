from vertex import Vertex

class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        numVertex = Vertex(key)
        self.vertList[key] = numVertex
        return numVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeigbhor(self.vertList[t],weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


graph = Graph()
for i in range(5):
    graph.addVertex(i)
print(graph.vertList)
graph.addEdge(0,1,2)
graph.addEdge(0,2,4)
graph.addEdge(1,2,3)
graph.addEdge(1,4,2)
graph.addEdge(2,3,2)
graph.addEdge(3,4,7)

for v in graph:
    for w in v.getConnections():
       print("( %s , %s )" % (v.getId(), w.getId()))