def floyd_warshall(graph):
    """
    Find the shortest paths between all pairs of nodes in a weighted directed graph using the Floyd-Warshall algorithm.
    
    Parameters:
        - graph: Dictionary where keys are nodes and values are dictionaries of neighbors with weights.

    Returns:
        - Distance matrix with the shortest path distances between all pairs of nodes.
    """
    # Initialize distance matrix
    vertices = list(graph.keys())
    distance_matrix = {vertex: {v: float('infinity') for v in vertices} for vertex in vertices}
    
    # Set the distance from each node to itself to 0
    for vertex in vertices:
        distance_matrix[vertex][vertex] = 0
    
    # Set the initial distances based on the graph edges
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            distance_matrix[vertex][neighbor] = weight
    
    # Apply the Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distance_matrix[i][j] > distance_matrix[i][k] + distance_matrix[k][j]:
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
    
    # Print output in the desired format
    print("All-pairs shortest paths:")
    for i in vertices:
        print("From node {}:".format(i))
        for j in vertices:
            if distance_matrix[i][j] == float('infinity'):
                print("{} to {}: inf".format(i, j))
            else:
                print("{} to {}: {}".format(i, j, distance_matrix[i][j]))

# Example graph
graph_floyd_warshall = { 
    'A': {'B': 1, 'C': 4}, 
    'B': {'C': 2, 'D': 5}, 
    'C': {'D': 1, 'E': 3}, 
    'D': {'E': 2, 'F': 6}, 
    'E': {'F': 2}, 
    'F': {}
}

# Run Floyd-Warshall algorithm
floyd_warshall(graph_floyd_warshall)
