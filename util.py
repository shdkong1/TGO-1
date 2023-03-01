# This file contains the utility functions used by the algorithms in this project.

def graph_builder(filename):
    graph = []

    file = open(filename)
    vertices = int(file.readline().removeprefix('vertices '))
    for i in range(vertices):
        graph_row = [float('inf')] * vertices
        graph_row[i] = 0
        graph.append(graph_row)

    for line in file:
        if 'vertices' in line:
            continue
        start, end, weight = line.split()
        graph[int(start) - 1][int(end) - 1] = int(weight)
        graph[int(end) - 1][int(start) - 1] = int(weight)

    file.close()
    return graph


def min_in_queue(queue, distances):
    distances_of_queue = []
    for i in queue:
        distances_of_queue.append(distances[i])
    minimum = min(distances_of_queue)
    return distances.index(minimum)


def find_neighbors(graph, index):
    vertex = graph[index]
    neighbors = []
    for i in range(len(vertex)):
        if vertex[i] > 0:
            neighbors.append(i)
    return neighbors


def trace(previous_list, start, end):
    current_vertex = end
    path = str(current_vertex + 1)
    while current_vertex != start:
        current_vertex = previous_list[current_vertex]
        path = str(current_vertex + 1) + ' -> ' + path
    return path
