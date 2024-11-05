from collections import deque

def bfs_weighted(graph, start):
    """ 
    Perform BFS traversal from the start node on a weighted directed graph.
    
    Parameters: 
        - graph: Dictionary where keys are nodes and values are dictionaries of neighbors with weights.
          Example: {'A': {'B': 5, 'C': 3}, 'B': {'C': 2, 'D': 4}, ...}
        - start: Starting vertex for BFS.
    
    Returns: 
        - List of nodes in the order they are visited.
    """
    visited = set()  # Set to keep track of visited vertices
    traversal_order = []  # List to store the order of traversal
    queue = deque([start])  # Initialize queue with the start node
    
    visited.add(start)  # Mark the start node as visited
    
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        traversal_order.append(vertex)  # Record the traversal order
        
        # Visit all unvisited adjacent vertices (ignoring weights for BFS traversal)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal_order

# Example weighted directed graph represented as an adjacency list with weights
graph = { 
    'A': {'B': 5, 'C': 3}, 
    'B': {'C': 2, 'D': 4}, 
    'C': {'E': 7}, 
    'D': {'E': 1, 'F': 8}, 
    'E': {'F': 2}, 
    'F': {}
} 

# Perform BFS traversal from the starting vertex 'A'
start_vertex = 'A'
result = bfs_weighted(graph, start_vertex)

# Display the result
print("BFS Traversal Order:", result)
