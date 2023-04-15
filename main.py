import random, time
import floyd_algo as floyd
from graph import Graph

# set size of the graph
n = 500

# initialize empty graphs with set size
sequential_graph = Graph(n)
parallel_graph = Graph(n)

# fill matrixes with random numbers in range [0,n)
for i in range(n):
    for j in range(n):
        random_number = random.randint(0, n)
        sequential_graph[i][j] = random_number
        parallel_graph[i][j] = random_number
print("Size: ", n)

# run sequential implementation of Floyd algorithm and measure time
start_sequential = time.time()
for k in range(n):
    floyd.floyd_sequential(sequential_graph, 0, n, k)
elapsed_sequential = time.time() - start_sequential

# run parallel implementation of Floyd algorithm and measure time
start_parallel = time.time()
for k in range(n):
    floyd.floyd_parallel(parallel_graph, 200, k)
elapsed_parallel = time.time() - start_parallel

# print results
print('Parallel Floyd: %f sec', (elapsed_parallel))
print('Sequential Floyd: %f sec', (elapsed_sequential))
print('Parallel is faster %f times', (elapsed_sequential / elapsed_parallel))

# check for mismatches between 2 implementation results
count = 0
for i in range(n):
    for j in range(n):
        if (sequential_graph[i][j] != parallel_graph[i][j]):
            count +=1
            print("Something went wrong in calculations")
            break
print("Different elements: %d", count)