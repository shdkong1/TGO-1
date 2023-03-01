import bellman_ford
import dijkstra


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
