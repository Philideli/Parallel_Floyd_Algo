import other_tries.sequential_floyd as sequential_floyd, other_tries.multiprocessing_floyd as multiprocessing_floyd
import time
import random

INF = 1000000

def generate_graph(size):
    graph = [[int(random.random()*INF) for i in range(size)] for i in range(size) ]
    # print(graph)
    return graph


if __name__ == '__main__':
    size = 50
    num_iterations = 3
    sequential_time = []
    multiprocessed_time = []

    for i in range(num_iterations):
        print(i)
        graph = generate_graph(size)

        start = time.time()
        matrix = sequential_floyd.floyd(graph)
        end = time.time()
        sequential_time.append(end-start)

        start = time.time()
        matrix = multiprocessing_floyd.floyd_multiprocessed(size, graph, size)
        end = time.time()
        multiprocessed_time.append(end-start)

    print(sequential_time)
    print(multiprocessed_time)