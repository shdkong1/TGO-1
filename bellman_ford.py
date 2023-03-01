# The Bellman-Ford Algorithm
# This algorithm computes the shortest path from a single source vertex
# to all the other vertices in a weighted graph. It is slower than Dijkstra's,
# but more versatile as it is capable of handling graphs in which some
# edge weights are negative numbers.

# The code below is adapted from the pseudocode as described in Wikipedia:
# https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm


def bellman_ford(graph, start):
    vertices = len(graph[0])

    distances = [float('inf')] * vertices
    distances[start] = 0

    previous = [-1] * vertices

    edges = build_edges(graph)

    iterations = 0

    for i in range(vertices - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                previous[v] = u
            iterations += 1

    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            print("Negative cycle detected")
        iterations += 1

    return previous, distances, iterations


def build_edges(graph):
    vertices = len(graph[0])
    edges = []
    for i in range(vertices):
        for j in range(vertices):
            if graph[i][j] != float('inf'):
                edges.append([i, j, graph[i][j]])
    return edges
