def floyd(graph):
    """
    Finds the shortest path between all pairs of vertices in a graph
    using Floyd's algorithm.

    :param graph: A 2D list representing the graph.
    :return: A 2D list representing the shortest path between all pairs of vertices.
    """
    n = len(graph)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # if graph[i][j] != 0:
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
