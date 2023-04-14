import sys, multiprocessing, random, time
from threading import Thread


class Matrix:
    inf = 9223372036854775807

    def __init__(self, ssize):
        self.size = ssize
        self.matrix = [[0 for x in range(ssize)] for x in range(ssize)]

    def __getitem__(self, i):
        return self.matrix[i]

    def Floyd(self, low, high, k):
        for i in range(int(low), int(high)):
            for j in range(self.size):
                if (self.matrix[i][k] != self.inf and self.matrix[k][j] != self.inf):
                    self.matrix[i][j] = min(self.matrix[i][k] + self.matrix[k][j], self.matrix[i][j])

    def RandomInput(self, a, b):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = random.randint(a, b)

    def Input(self, i, j, value=inf):
        self.matrix[i][j] = value

    def Print(self):
        for i in range(self.size):
            for j in range(self.size):
                if (self.matrix[i][j] == self.inf):
                    print("inf\t", end='')
                else:
                    print(self.matrix[i][j], "\t", end='')
            print()

    def Parallel(self, numProc, k):
        begin = []
        end = []

        begin.append(0)
        end.append(self.size / numProc)  # 1

        for i in range(1, numProc - 1):
            begin.append(begin[i - 1] + end[0])  # 1   2
            end.append(end[i - 1] + end[0])  # 2   3
        begin.append(begin[numProc - 2] + end[0])
        end.append(self.size)
        threads = []
        for i in range(numProc):
            threads.append(Thread(target=self.Floyd, args=(begin[i], end[i], k)))

        for foo in threads:
            foo.start()

        for foo in threads:
            foo.join()