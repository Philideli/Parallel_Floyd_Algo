import random, time
import floyd_algo as floyd
from graph import Graph
import other_tries.multiprocessing_floyd as floyd_legacy
import multiprocessing as mp

# set size of the graph
n = 10
PROC_CNT = 4

# initialize empty graphs with set size
sequential_graph = Graph(n)
parallel_graph = Graph(n)

# fill matrixes with random numbers in range [0,n)
for i in range(n):
    for j in range(n):
        random_number = random.randint(0, sequential_graph.inf)
        if random_number == sequential_graph.inf:
            random_number = -1
        sequential_graph[i][j] = random_number
        parallel_graph[i][j] = random_number
print("Size: ", n)

# run sequential implementation of Floyd algorithm and measure time
start_sequential = time.time()
for k in range(n):
    floyd.floyd_sequential(sequential_graph, 0, n,0,n, k)
elapsed_sequential = time.time() - start_sequential


# run parallel implementation of Floyd algorithm and measure time
start_parallel = time.time()
parallel_graph = floyd.floyd_parallel(n, parallel_graph, 8)
elapsed_parallel = time.time() - start_parallel

# print results
print(f'Parallel Floyd: {elapsed_parallel} sec')
print(f'Sequential Floyd: {elapsed_sequential} sec')
print(f'Parallel is faster {elapsed_sequential / elapsed_parallel} times')

# check for mismatches between 2 implementation results
count = 0
for i in range(n):
    for j in range(n):
        if (sequential_graph[i][j] != parallel_graph[i][j]):
            count +=1
            print("Something went wrong in calculations")
            break
print(f"Different elements: {count}")


