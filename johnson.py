# Johnson's Algorithm
# This algorithm is a way to find the shortest paths between all pairs
# of vertices in an edge-weighted directed graph. It allows some of the edge
# weights to be negative numbers. It works by using the Bellman-Ford algorithm
# to compute a transformation of the input graph that removes all negative weights.
# This allows Dijkstra's algorithm to be used on the transformed graph.

import bellman_ford
import dijkstra

# The code below is adapted from the pseudocode as described in Wikipedia:
# https://en.wikipedia.org/wiki/Johnson%27s_algorithm


def johnson(graph, start, end):
    vertices = len(graph[0])

    for i in graph:
        i.append(0)
    new_vertex = [0 for i in range(vertices + 1)]
    graph.append(new_vertex)

    previous, distances, iterations = \
        bellman_ford.bellman_ford(graph, vertices)
    distances.pop()

    modified_graph = [[0 for i in range(vertices)] for j in range(vertices)]
    for i in range(vertices):
        for j in range(vertices):
            if graph[i][j] != float('inf'):
                modified_graph[i][j] = \
                    (graph[i][j] + distances[i] - distances[j])

    prev_iterations = iterations
    previous, distances, iterations =  \
        dijkstra.dijkstra(modified_graph, start, end)
    iterations += prev_iterations

    return previous, distances, iterations
