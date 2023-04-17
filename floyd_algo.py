import multiprocessing as mp
from threading import Thread

def floyd_sequential(graph):
    n = graph.size
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (graph[i][k] >= 0 and graph[k][j] >= 0):
                    graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    return graph

def init_parallel_simple(dists_arr):
    global dists
    dists = dists_arr

def floyd_parallel_simple(graph_initial, n):
    # unwrap the 2d graph of edges to a 1d array with i * n + j indexation
    graph_unwrapped = []
    for row in graph_initial:
        graph_unwrapped += row
    
    # create a synchronized array that will be available to all processes
    # we don't need locking, because we only use this distance array
    # for 3rd loop of Floyd's algorithm, which is independent
    # of other other iterations
    graph_unwrapped_synced = mp.Array('i', graph_unwrapped, lock=False)

    for k in range(n):
        # the pool that executes the 3rd loop of Floyd's algorithm
        # here we initialize the dist array
        # so that it is available inside the worker functions
        pool = mp.Pool(initializer=init_parallel_simple, initargs=(graph_unwrapped_synced,))
        # for each i (2nd loop of Floyd's algorithm)
        # we execute all loops for j (3rd loop) in parallel
        pool.map(worker_simple, [(n, k, i) for i in range(n)])
        # finalize parallelization and sync results
        pool.close()
        pool.join()
        
    # bring back the distances representation to 2d-array
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(graph_unwrapped_synced[i * n + j])
        result.append(row)

    return result


def worker_simple(args):
    n, k, i = args
    # important: use the synced array between processes
    global dists
    # 3rd loop of Floyd's algorithm
    for j in range(n):
        if (dists[i * n + k] >= 0 and dists[k * n + j] >= 0):
            v = min(dists[i * n + j], dists[i * n + k] + dists[k * n + j])
            dists[i * n + j] = v