import util


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
