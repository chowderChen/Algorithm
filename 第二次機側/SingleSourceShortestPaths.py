# Single source shortest paths

INFINITY = 1e30

class AdjacencyMatrix:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.n_edges = 0
        self.A = [[0 for j in range(n_vertices + 1)] for i in range(n_vertices + 1)]

        self.d = [0 for i in range(n_vertices + 1)]
        self.pi = [0 for i in range(n_vertices + 1)]
        self.f = [0 for i in range(n_vertices + 1)]

        self.time = 0
        self.TS_list = []

    def SetDirectedEdgeWeight(self, start_vertex, end_vertex, weight):
        if (start_vertex >= 1 and start_vertex <= self.n_vertices and
                end_vertex >= 1 and end_vertex <= self.n_vertices):
            if (self.A[start_vertex][end_vertex] == 0):
                self.A[start_vertex][end_vertex] = weight
                self.n_edges += 1

    def Display(self):
        print("Graph (Adjacency Matrix Representation)")
        print("Number of Vertices =", self.n_vertices)
        print("Number of Edges =", self.n_edges)
        for i in range(1, self.n_vertices + 1):
            for j in range(1, self.n_vertices + 1):
                print(self.A[i][j], end=" ")
            print()

    def Dijkstra(self, source):
        # Initialization
        for i in range(1, self.n_vertices + 1):
            self.d[i] = INFINITY
        self.d[source] = 0
        self.pi[source] = 0

        set = [True] * (self.n_vertices + 1)

        n = self.n_vertices
        while (n != 0):
            # Extract Minimum
            u = 0
            min = INFINITY
            for i in range(1, self.n_vertices + 1):
                if (set[i] and self.d[i] < min):
                    u = i
                    min = self.d[i]
            set[u] = False
            n -= 1

            # Relax
            for v in range(1, self.n_vertices + 1):
                if (self.A[u][v] != 0):
                    if (self.d[v] > self.d[u] + self.A[u][v]):
                        self.d[v] = self.d[u] + self.A[u][v]
                        self.pi[v] = u

        # print("Dijkstra Algorithm:")
        for i in range(1, self.n_vertices + 1):
            if i != sourceVortexId:
                print( sourceVortexId, "to", i, "=", self.d[i])
            # print("Vertex", i, "Distance to source =", self.d[i], "Parent =", self.pi[i])

if __name__ == '__main__':
    run = True
    while run:
        vortexNum = int(input( "number of vortex: " ))
        if vortexNum == 0:
            run = False
        else:
            edgeNum = int(input())
            sourceVortexId = int(input())
            adjM = AdjacencyMatrix( vortexNum )
            for i in range(edgeNum):
                relation = input()
                relation = list(map(int, relation.split() ))
                adjM.SetDirectedEdgeWeight( relation[0], relation[1], relation[2] )
            adjM.Dijkstra( sourceVortexId )
            print()
