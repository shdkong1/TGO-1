import util


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
