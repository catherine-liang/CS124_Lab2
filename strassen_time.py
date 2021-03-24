from random import randint
from math import ceil, floor
import sys
import time

def matmult(a, b):
    #z_b = list(zip(*b))
    #return [[sum(x * y for x, y in zip(a_row, b_col)) for b_col in z_b] for a_row in a]
# iterate through rows of X
    result = [ [0]*len(a) for i in range(len(a)) ]
    for i in range(len(a)):
       # iterate through columns of Y
       for j in range(len(b)):
           # iterate through rows of Y
           for k in range(len(a)):
               result[i][j] += a[i][k] * a[k][j]
    return result



def matadd(a, b):
    return [[x + y for x, y in zip(col_a, col_b)] for col_a, col_b in zip(a, b)]

def matsub(a, b):
    return [[x - y for x, y in zip(col_a, col_b)] for col_a, col_b in zip(a, b)]

def readfile(filename, d):
    dims = range(d)
    a = [[0 for i in dims] for j in dims]
    b = [[0 for i in dims] for j in dims]
    with open(filename) as f:
        i = 0
        j = 0
        for line in f:
            if i < d:
                a[i][j] = int(line.strip())
                j += 1
                if j > d-1:
                    j = 0
                    i += 1
            else:
                b[i-d][j] = int(line.strip())
                j += 1
                if j > d-1:
                    j = 0
                    i += 1
    return a, b


def strassens(a, b, crossover):
    n = len(a)

    if n <= crossover:
        return matmult(a, b)

    else:
        range_n = range(n)
        if n%2 != 0:
            nx = n + 1
            #pad with zeros
            a = [a[i] + [0] for i in range_n] + [[0] * nx]
            b = [b[i] + [0] for i in range_n] + [[0] * nx]

        else:
            nx = n

        cut = nx//2
        fronth = range(0, cut)
        backh = range(cut, nx)

        A = [a[i][:cut] for i in fronth]
        B = [a[i][cut:nx] for i in fronth]
        C = [a[i][:cut] for i in backh]
        D = [a[i][cut:nx] for i in backh]
        E = [b[i][:cut] for i in fronth]
        F = [b[i][cut:nx] for i in fronth]
        G = [b[i][:cut] for i in backh]
        H = [b[i][cut:nx] for i in backh]

        P1 = strassens(A, matsub(F, H), crossover=crossover)
        P2 = strassens(matadd(A, B), H, crossover=crossover)
        P3 = strassens(matadd(C, D), E, crossover=crossover)
        P4 = strassens(D, matsub(G, E), crossover=crossover)
        P5 = strassens(matadd(A, D), matadd(E, H), crossover=crossover)
        P6 = strassens(matsub(B, D), matadd(G, H), crossover=crossover)
        P7 = strassens(matsub(A, C), matadd(E, F), crossover=crossover)

        result = list(map(lambda x,y:x+y, matadd(matsub(matadd(P5, P4), P2), P6), matadd(P1, P2)))
        result.extend(list(map(lambda x,y:x+y, matadd(P3, P4), matsub(matsub(matadd(P5, P1), P3), P7))))
        return [result[i][:n]for i in range_n]


if __name__ == "__main__":
    # crossover_val = 0
    # while crossover_val <= 120:

    #     dimension = 500
    #     crossover_val += 1
    #     tic = time.perf_counter()
    #     a = [ [1]*dimension for i in range(dimension) ]
    #     product = strassens(a, a, crossover=crossover_val)
    #     toc = time.perf_counter()

    #     print(f"crossover:{crossover_val} - finished in {toc - tic:0.4f} seconds")

    #crossover_val = 1
    dimension = 0

    while dimension <= 250:
        dimension += 2
        ##crossover_val = dimension - 1
        crossover_val = 400
        tic = time.perf_counter()
        a = [ [1]*dimension for i in range(dimension) ]
        product = strassens(a, a, crossover=crossover_val)
        toc = time.perf_counter()

        print(f"{toc - tic:0.4f}")


  

    # dimension = 1024

    # p = 0.04


    # a = [ [0]*dimension for _ in range(dimension) ]
    

    # ##a, b = read_file(filename, dimension)
    # for i in range(dimension):
    #     for j in range(i):
    #         if (uniform(0.00, 1.00) <= p):
    #             a[i][j] = 1;
    #             a[j][i] = 1;


    # product = strassens(a, strassens(a, a, crossover=128))


    # sum = 0.00
    # for i in range(dimension):
    #     sum += product[i][i]

    # print(sum/6.00)
