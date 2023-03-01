# The A* Algorithm
# This algorithm (pronounced "A-star") is a graph traversal and path search
# algorithm. It can be seen as an extension of Dijkstra's algorithm. It achieves
# better performance by using heuristics to guide its search.

import util

# The code below is adapted from the pseudocode as described in Wikipedia:
# https://en.wikipedia.org/wiki/A*_search_algorithm


def a_star(graph, start, end):
    vertices = len(graph[0])

    distances = [float('inf')] * vertices
    distances[start] = 0

    closest_neighbor = [float('inf')] * vertices
    closest_neighbor[start] = min(graph[start])

    previous = [-1] * vertices

    queue = list(range(vertices))

    iterations = 0

    while len(queue) != 0:
        current_vertex = util.min_in_queue(queue, closest_neighbor)
        if current_vertex is end:
            break
        queue.remove(current_vertex)

        neighbors = util.find_neighbors(graph, current_vertex)
        for neighbor in neighbors:
            distance_to_neighbor = distances[current_vertex] \
                                   + graph[current_vertex][neighbor]
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                closest_neighbor[neighbor] = distance_to_neighbor + min(graph[neighbor])
                previous[neighbor] = current_vertex
                if neighbor not in queue:
                    queue.append(neighbor)
        iterations += 1

    return previous, distances, iterations
