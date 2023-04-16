from threading import Thread
import multiprocessing as mp

def floyd_sequential(graph, low_i, high_i, low_j, high_j, k):
    for i in range(int(low_i), int(high_i)):
        for j in range(int(low_j), int(high_j)):
            if (graph[i][k] >= 0 and graph[k][j] >= 0):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])


def floyd_parallel(self):
    n = self.size
    

    mp.set_start_method('fork')
    for k in range(n):
        processes: list[mp.Process] = []
        for i in range(n):
            process = mp.Process(target=self.worker, args=(k, i))
            processes.append(process)
            process.start()
    
        for p in processes:
            p.join()
            # print(self.graph)
            # print('=-----------------')
    return self.graph


def worker(self, k, i):
    # print(f"thread {k} start")
    n = self.size
    for j in range(n):
        self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])
    # print(f"thread {k} end")