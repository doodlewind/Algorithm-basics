class MST:
    def __init__(self, graph):
        self.graph = graph
        self.conn_comps = [set(vertex) for vertex in graph]
        self.visited, self.edges, self.edges_chosen = [], [], []
        for v in self.graph:
            for adg_v in graph[v]:
                if self.find_edges(v, adg_v):
                    self.edges.append([{v, adg_v}, self.graph[v][adg_v]])
        self.edges = sorted(self.edges, key=lambda x: x[1])

    def find_edges(self, v1, v2):
        for edge in self.edges:
            if v1 in edge[0] and v2 in edge[0]:
                return False
        return True

    def kruskal(self):
        while len(self.conn_comps) > 1:
            self.choose_edge()

    def choose_edge(self):
        tmp_edge = self.edges[0]
        self.union(tmp_edge)

    def union(self, edge):
        flag = False
        idx = 0
        for comp in self.conn_comps:
            inter = edge[0].intersection(comp)
            if len(inter) == 1:
                comp.update(edge[0])
                flag = True
                idx = self.conn_comps.index(comp)
                break
        if flag:
            for i in range(0, len(self.conn_comps)):
                if i == idx:
                    continue
                if len(self.conn_comps[i].intersection(comp)) > 0:
                    comp.update(self.conn_comps[i])
                    self.edges_chosen.append(edge)
                    del self.conn_comps[i]
                    del self.edges[0]
                    break
        else:
            del self.edges[0]

if __name__ == '__main__':
    test_graph = {
       'A': {'B': 7, 'D': 5},
       'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
       'C': {'B': 8, 'E': 5},
       'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
       'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
       'F': {'D': 6, 'E': 8, 'G': 11},
       'G': {'E': 9, 'F': 11}
    }

    m = MST(test_graph)
    m.kruskal()
    print m.edges_chosen