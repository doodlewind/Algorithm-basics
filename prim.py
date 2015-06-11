class MST:
    def __init__(self, graph):
        self.graph = graph
        self.visited, self.unvisited, self.edges = [], [], []
        for node in self.graph:
            self.unvisited.append(node)
        self.visited.append(self.unvisited[0])
        del(self.unvisited[0])

    def prim(self):
        while len(self.visited) < len(self.graph):
            node_chosen = self.choose_node()
            self.visited.append(node_chosen)
            self.unvisited.remove(node_chosen)
        return self.edges

    def choose_node(self):
        tmp_edge = []
        for un_node in self.unvisited:
            for adj_node in test_graph[un_node]:
                if adj_node in self.visited:
                    tmp_edge.append([{un_node, adj_node}, self.graph[un_node][adj_node]])
        edge_chosen = min(tmp_edge, key=lambda x: x[1])
        self.edges.append(edge_chosen)

        for node in edge_chosen[0]:
            if node in self.unvisited:
                return node


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
    print m.prim()