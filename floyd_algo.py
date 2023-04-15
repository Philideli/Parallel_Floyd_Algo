from threading import Thread

def floyd_sequential(graph, low, high, k):
    for i in range(int(low), int(high)):
        for j in range(graph.size):
            if (graph[i][k] != graph.inf and graph[k][j] != graph.inf):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

def floyd_parallel(graph, numProc, k):
    begin = []
    end = []

    begin.append(0)
    end.append(graph.size / numProc) 

    for i in range(1, numProc - 1):
        begin.append(begin[i - 1] + end[0]) 
        end.append(end[i - 1] + end[0]) 
    begin.append(begin[numProc - 2] + end[0])
    end.append(graph.size)
    threads = []
    for i in range(numProc):
        threads.append(Thread(target=floyd_sequential, args=(graph,begin[i], end[i], k)))

    for foo in threads:
        foo.start()

    for foo in threads:
        foo.join()