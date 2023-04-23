from multiprocessing import Array as SynchronizedArray
from concurrent.futures import ProcessPoolExecutor

def floyd_sequential(graph):
    n = graph.size
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (graph[i][k] >= 0 and graph[k][j] >= 0):
                    graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    return graph

def floyd_parallel(graph):
    n = graph.size  
    # unwrap the 2d graph of edges to a 1d array with i * n + j indexation
    # and also implicitely create a shallow copy of the graph
    graph_unwrapped = []
    for row in graph:
        graph_unwrapped += row
    # create a synchronized array that will be available to all processes
    # we don't need locking, because we only use this distance array
    # for 3rd loop of Floyd's algorithm, which is independent
    # of other other iterations
    graph_unwrapped_synced = SynchronizedArray('i', graph_unwrapped, lock=False)
    # the pool that executes the 3rd loop of Floyd's algorithm
    # here we initialize the dist array
    # so that it is available inside the worker functions
    with ProcessPoolExecutor(max_workers=4, initializer=init_parallel, initargs=(graph_unwrapped_synced,)) as executor:
        for k in range(n):
            # for each i (2nd loop of Floyd's algorithm)
            # we execute all loops for j (3rd loop) in parallel
            print(k)
            for i in range(n):
                executor.submit(worker, n, k, i)
    # notice: we don't need to wait for all processes to finish in each iteration of the
    # k loop, because the i loop processes are independent
    # -------------------------------------------------
    # bring back the distances representation to 2d-array
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(graph_unwrapped_synced[i * n + j])
        result.append(row)
    return result


def init_parallel(dists_arr):
    # making the shared memory variable global
    # makes sure that it is accessible from all process workers
    # any other configurations do not allow concurrent updates
    global dists
    dists = dists_arr


def worker(n, k, i):
    # important: use the synced array between processes
    # ---------------------------------------------
    # 3rd loop of Floyd's algorithm
    for j in range(n):
        if (dists[i * n + k] >= 0 and dists[k * n + j] >= 0):
            v = min(dists[i * n + j], dists[i * n + k] + dists[k * n + j])
            dists[i * n + j] = v