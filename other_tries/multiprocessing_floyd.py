import multiprocessing as mp

def floyd_multiprocessed(n, graph, process_count):
    # Initialize the dist matrix
    dist = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    with mp.Manager() as manager:
        matrix = manager.list()
        for row in dist:
            matrix.append(row)
        
        lock = mp.Lock()

        # Perform the Floyd-Warshall algorithm
        for k in range(n):
            processes = []

            # Start process_count processes to compute the k-th column of the dist matrix
            for i in range(process_count):
                p = mp.Process(target=floyd_process, args=(n, matrix, k, i, process_count, lock))
                processes.append(p)
                p.start()

            # Wait for all processes to finish
            for p in processes:
                p.join()
        matrix = str(matrix)
    return matrix

def floyd_process(n, dist, k, i, process_count, lock):
    # for i in range(process_id, n, process_count):
    for j in range(n):
        lock.acquire()
        row = dist[i]
        row[j] = min(dist[i][j], dist[i][k] + dist[k][j])
        dist[i] = row
        lock.release()