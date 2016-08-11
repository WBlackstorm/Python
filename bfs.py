class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.color = 'black'
        self.distance = -1

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def bfs(self, starting_vertex):
        q = list()
        starting_vertex.distance = 0
        starting_vertex.color = 'red'

        for v in starting_vertex.neighbors:
            self.vertices[v].distance = starting_vertex.distance + 6
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                if v in q:
                    continue

                node_v = self.vertices[v]

                if node_v.color == 'black':
                    q.append(v)
                    #if node_v.distance > node_u.distance + 6 | node_v.distance < 0:
                    #    node_v.distance = node_u.distance + 6
                    node_v.distance = node_u.distance + 6


testcase = int(input())

while testcase > 0:
    g = Graph()

    first_line = input().split()
    vertices = int(first_line[0])
    edges = int(first_line[1])

    for v in range(1, vertices + 1):
        vertex = Vertex(v)
        g.add_vertex(vertex)

    for read in range(edges):
        edge = input().split()
        vert1 = int(edge[0])
        vert2 = int(edge[1])

        g.vertices[vert1].add_neighbor(vert2)
        g.vertices[vert2].add_neighbor(vert1)

    start = int(input())

    g.bfs(g.vertices[start])
    testcase = testcase - 1

    response = ''

    for key, value in g.vertices.items():
        if (start != key):
            response = response + str(value.distance) + ' '

    print(response)
        
