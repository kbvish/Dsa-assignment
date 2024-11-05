import heapq

def dijkstra(graph, source):
    """
    Find the shortest path from the source node to all other nodes in a weighted directed graph.

    Parameters:
        - graph: Dictionary where keys are nodes and values are dictionaries of neighbors with weights.
        - source: Starting vertex for Dijkstra's algorithm.

    Returns:
        - Dictionary of shortest distances from source to each node.
    """
    # Initialize distances
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]  # Priority queue to hold nodes and their distances from the source

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If this distance is already greater than the recorded shortest distance, skip processing
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Print output in the desired format
    print("Shortest paths from source node {}:".format(source))
    for vertex, distance in distances.items():
        print("{} to {}: {}".format(source, vertex, distance))

# Example graph
graph_dijkstra = { 
    'A': {'B': 1, 'C': 4}, 
    'B': {'C': 2, 'D': 5}, 
    'C': {'D': 1, 'E': 3}, 
    'D': {'E': 2, 'F': 6}, 
    'E': {'F': 2}, 
    'F': {}
} 

# Run Dijkstra's algorithm from the starting vertex 'A'
dijkstra(graph_dijkstra, 'A')
