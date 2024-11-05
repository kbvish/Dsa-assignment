import heapq

def prim(graph, start_vertex):
    mst = []
    visited = set()
    min_heap = [(0, start_vertex)]  # (weight, vertex)
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            mst.append((weight, u))
            
            for v, edge_weight in graph['adjacency_list'][u]:
                if v not in visited:
                    heapq.heappush(min_heap, (edge_weight, v))
    
    return mst

# Example usage for Prim's Algorithm
graph_prim = {
    'adjacency_list': {
        0: [(1, 10), (2, 6), (3, 5)],
        1: [(0, 10), (3, 15)],
        2: [(0, 6), (3, 4)],
        3: [(0, 5), (1, 15), (2, 4)]
    }
}

mst_prim = prim(graph_prim, 0)
print("Prim's MST:", mst_prim)
