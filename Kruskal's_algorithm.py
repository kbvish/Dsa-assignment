class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph):
    edges = sorted(graph['edges'], key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(graph['vertices'])
    mst = []
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):  # Check if adding this edge forms a cycle
            ds.union(u, v)
            mst.append((u, v, weight))
    return mst

# Example usage for Kruskal's Algorithm
graph_kruskal = {
    'vertices': 4,
    'edges': [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
}

mst_kruskal = kruskal(graph_kruskal)
print("Kruskal's MST:", mst_kruskal)
