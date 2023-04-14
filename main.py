import random, time
import floyd_algo

n = 500

b = floyd_algo.Matrix(n)
c = floyd_algo.Matrix(n)
for i in range(n):
    for j in range(n):
        lol = random.randint(0, n)
        b[i][j] = lol
        c[i][j] = lol

print("Size: ", n)
for i in range(n):
    for j in range(n):
        if (b[i][j] != c[i][j]):
            print("Bad arrays to compare!")
            break

start1 = time.time()
for k in range(n):
    b.Floyd(0, n, k)
elapsed1 = time.time() - start1
start2 = time.time()
for k in range(n):
    c.Parallel(200, k)
elapsed2 = time.time() - start2

print('Parallel Floyd: %f sec' % (elapsed2))
print('Sequential Floyd: %f sec' % (elapsed1))
print('Parallel is faster %f times' % (elapsed1 / elapsed2))

count = 0

for i in range(n):
    for j in range(n):
        if (b[i][j] != c[i][j]):
            count += 1
            print("Something went wrong in calculations")
            break

print("Different elements: ", count)