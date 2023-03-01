# The Floyd-Warshall Algorithm
# This algorithm finds the shortest paths in a directed weighted graph with
# positive or negative edge weights (but with no negative cycles). A single
# execution of the algorithm will find the lengths of the shortest paths between
# all pairs of vertices. Although it does not return details of the paths
# themselves, it is possible to reconstruct the paths with simple modifications
# to the algorithm.

# The code below is adapted from the pseudocode as described in Wikipedia:
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

def floyd_warshall(graph, start, end):
    vertices = len(graph[0])

    iterations = 0

    next_nodes = [[0 for j in range(vertices)] for i in range(vertices)]
    for i in range(vertices):
        for j in range(vertices):
            if graph[i][j] != 0:
                next_nodes[i][j] = j
            if i == j:
                next_nodes[i][j] = j
            iterations += 1

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    next_nodes[i][j] = next_nodes[i][k]
                iterations += 1

    return next_nodes, graph, iterations


def construct_path(next_nodes, start, end):
    path = str(start + 1)
    while start != end:
        start = next_nodes[start][end]
        path = path + ' -> ' + str(start + 1)
    return path
