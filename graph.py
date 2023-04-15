import random

class Graph:
    inf = 9223372036854775807

    def __init__(self, size):
        self.size = size
        self.graph = [[0 for x in range(size)] for x in range(size)]

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