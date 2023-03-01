# Dijkstra's Algorithm
# This algorithm finds the shortest paths between nodes in a weighted graph.
# The algorithm exists in many variants. Dijkstra's original algorithm found
# the shortest path between two given nodes, but a more common variant fixes
# a single node as the source node and finds the shortest paths to all ohter
# nodes in the graph.

import util

# The code below is adapted from the pseudocode as described in Wikipedia:
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm


def dijkstra(graph, start, end):
    vertices = len(graph[0])

    distances = [float('inf')] * vertices
    distances[start] = 0

    previous = [-1] * vertices

    queue = list(range(vertices))

    iterations = 0

    while len(queue) != 0:
        current_vertex = util.min_in_queue(queue, distances)
        if current_vertex is end:
            break
        queue.remove(current_vertex)

        neighbors = util.find_neighbors(graph, current_vertex)
        for neighbor in neighbors:
            distance_to_neighbor = distances[current_vertex] \
                                   + graph[current_vertex][neighbor]
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                previous[neighbor] = current_vertex

        iterations += 1

    return previous, distances, iterations
