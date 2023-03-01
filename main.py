import a_star
import bellman_ford
import dijkstra
import floyd_warshall
import johnson
import util


if __name__ == '__main__':
    start = 0
    end = 10

    previous, distances, iterations = \
        dijkstra.dijkstra(util.graph_builder('graph.txt'), start, end)
    print("-- Dijkstra's Algorithm --")
    print('Path:', util.trace(previous, start, end))
    print('Distance:', distances[end])
    print('Iterations:', iterations)

    previous, distances, iterations = \
        bellman_ford.bellman_ford(util.graph_builder('graph.txt'), start)
    print("-- Bellman-Ford Algorithm --")
    print('Path:', util.trace(previous, start, end))
    print('Distance:', distances[end])
    print('Iterations:', iterations)

    previous, distances, iterations = \
        a_star.a_star(util.graph_builder('graph.txt'), start, end)
    print("-- A* Algorithm --")
    print('Path:', util.trace(previous, start, end))
    print('Distance:', distances[end])
    print('Iterations:', iterations)

    next_nodes, graph, iterations = \
        floyd_warshall.floyd_warshall(util.graph_builder('graph.txt'), start, end)
    print('-- Floyd-Warshall Algorithm --')
    print('Path:', floyd_warshall.construct_path(next_nodes, start, end))
    print('Distance:', graph[start][end])
    print('Iterations:', iterations)

    previous, distances, iterations = \
        johnson.johnson(util.graph_builder('graph.txt'), start, end)
    print("-- Johnson's Algorithm --")
    print('Path:', util.trace(previous, start, end))
    print('Distance:', distances[end])
    print('Iterations:', iterations)
