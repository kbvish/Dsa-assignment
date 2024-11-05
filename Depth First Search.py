def dfs_weighted(graph, start, visited=None, traversal_order=None):
    """
    Perform DFS traversal from the start node on a weighted directed graph.

    Parameters:
    - graph: Dictionary where keys are nodes and values are dictionaries of neighbors with weights.
             Example: {'A': {'B': 5, 'C': 3}, 'B': {'C': 2, 'D': 4}, ...}
    - start: Starting vertex for DFS
    - visited: Set of visited nodes (used for recursion, initially None)
    - traversal_order: List to store the order of traversal (used for recursion, initially None)
    
    Returns:
    - List of nodes in the order they are visited
    """
    if visited is None:
        visited = set()  # Initialize visited set if not provided
    if traversal_order is None:
        traversal_order = []  # Initialize traversal order list if not provided

    # Mark the starting vertex as visited and add it to traversal order
    visited.add(start)
    traversal_order.append(start)

    # Recursively visit all unvisited adjacent vertices (ignoring weights for DFS traversal)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_weighted(graph, neighbor, visited, traversal_order)

    return traversal_order

# New example weighted directed graph represented as an adjacency list with weights
graph = {
    '1': {'2': 10, '3': 5},
    '2': {'4': 7, '5': 1},
    '3': {'5': 9, '6': 2},
    '4': {'7': 3},
    '5': {'4': 6, '7': 4, '8': 8},
    '6': {'8': 3},
    '7': {'9': 11},
    '8': {'9': 4},
    '9': {}
}

# Perform DFS traversal from the starting vertex '1'
start_vertex = '1'
result = dfs_weighted(graph, start_vertex)

# Display the result
print("DFS Traversal Order:", result)
