import random
import multiprocessing as mp

class Graph:
    inf = 10 #9223372036854775807

    def __init__(self, size):
        self.size = size
        self.graph = [[0 for x in range(size)] for x in range(size)]
        # self.grah = [[-1,1,2,4,5],[4,-1,4,1,2],[2,0,-1,1,1],[-1,0,-1,-1,2],[0,0,2,-1,-1]] 

    def __getitem__(self, i):
        return self.graph[i]

    def random_input(self, a, b):
        for i in range(self.size):
            for j in range(self.size):
                self.graph[i][j] = random.randint(a, b)

    def input(self, i, j, value=inf):
        self.graph[i][j] = value

    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                if (self.graph[i][j] == self.inf):
                    print("inf\t", end='')
                else:
                    print(self.graph[i][j], "\t", end='')
            print()