import random
import time
import floyd_algo as floyd
from graph import Graph

# set size of the graph
N = 50
NUM_TESTS = 1
PROC_CNT = 4

# initialize empty lists for time measurements
sequential_time = []
parallel_time = []

# initialize empty graphs with set size
sequential_graph = Graph(N)
parallel_graph = Graph(N)


def generate_random_graphs():
    ''' fill matrixes with random numbers in range [0,n) '''
    for i in range(N):
        for j in range(N):
            random_number = random.randint(0, sequential_graph.inf)
            if random_number == sequential_graph.inf:
                random_number = -1
            sequential_graph[i][j] = random_number
            parallel_graph[i][j] = random_number


def check_for_mismatches():
    '''check for mismatches between 2 implementation results '''
    count = 0
    for i in range(N):
        for j in range(N):
            if (sequential_graph[i][j] != parallel_graph[i][j]):
                count += 1
                print("Something went wrong in calculations")
                break
    print(f"Different elements: {count}")


def time_results(sequential_time_results, parallel_time_results):
    '''calculate and print time measurement results
        Args:
            sequential_time_results (list): sequential implementation time measurements
            parallel_time_results (list): parallel implementation time measurements
    '''
    average_sequential = sum(sequential_time_results) / NUM_TESTS
    average_parallel = sum(parallel_time_results) / NUM_TESTS
    print(f'Sequential Floyd: {average_sequential} sec')
    print(f'Parallel Floyd: {average_parallel} sec')
    print(f'Parallel is faster {average_sequential / average_parallel} times')


if __name__ == '__main__':
    for test in range(NUM_TESTS):
        # fill matrixes with random numbers in range [0,n)
        generate_random_graphs()

        # run sequential implementation of Floyd algorithm and measure time
        start_sequential = time.time()
        sequential_graph = floyd.floyd_sequential(sequential_graph)
        sequential_time.append(time.time() - start_sequential)

        # run parallel implementation of Floyd algorithm and measure time
        start_parallel = time.time()
        parallel_graph = floyd.floyd_parallel_simple(parallel_graph, N)
        parallel_time.append(time.time() - start_parallel)

        # check for mismatches between 2 implementation results
        check_for_mismatches()

    # print time results
    time_results(sequential_time, parallel_time)
