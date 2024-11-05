def bellman_ford(graph, source):
    """
    Find the shortest path from the source node to all other nodes in a weighted directed graph.
    
    Parameters:
        - graph: Dictionary where keys are nodes and values are dictionaries of neighbors with weights.
        - source: Starting vertex for the Bellman-Ford algorithm.
    
    Returns:
        - Dictionary of shortest distances from source to each node if no negative weight cycle is present.
    """
    # Initialize distances
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0

    # Relax all edges V-1 times
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Check for negative weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                print("Graph contains a negative weight cycle")
                return

    # Print output in the desired format
    print("Shortest paths from source node {}:".format(source))
    for vertex, distance in distances.items():
        print("{} to {}: {}".format(source, vertex, distance))

# Example graph
graph_bellman_ford = { 
    'A': {'B': 1, 'C': 4}, 
    'B': {'C': 2, 'D': 5}, 
    'C': {'D': 1, 'E': 3}, 
    'D': {'E': 2, 'F': 6}, 
    'E': {'F': 2}, 
    'F': {}
} 

# Run Bellman-Ford algorithm from the starting vertex 'A'
bellman_ford(graph_bellman_ford, 'A')
