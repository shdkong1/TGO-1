import util


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