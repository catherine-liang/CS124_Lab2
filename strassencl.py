from random import randint
from math import ceil, floor
import sys

def matmult(a, b):
    z_b = list(zip(*b))
    return [[sum(x * y for x, y in zip(a_row, b_col)) for b_col in z_b] for a_row in a]

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


def strassens(a, b, crossover=2):
    n = len(a)

    if n <= crossover:
        return matmult(a, b)

    else:
        range_n = range(n)
        if n%2 != 0:
            nx = n + 1
            #pad with zeros
            #a = [a[i] + [0] for i in range_n] + [[0] * nx]
            #b = [b[i] + [0] for i in range_n] + [[0] * nx]

            a = [a[i] + [0]] + [[0]]
            b = [b[i] + [0]] + [[0]]

        else:
            nx = n

        split = nx//2
        first_half = range(0, split)
        second_half = range(split, nx)

        A = [a[i][:split] for i in first_half]
        B = [a[i][split:nx] for i in first_half]
        C = [a[i][:split] for i in second_half]
        D = [a[i][split:nx] for i in second_half]
        E = [b[i][:split] for i in first_half]
        F = [b[i][split:nx] for i in first_half]
        G = [b[i][:split] for i in second_half]
        H = [b[i][split:nx] for i in second_half]

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
    flag = int(sys.argv[1])
    dimension = int(sys.argv[2])
    filename = sys.argv[3]

    a, b = readfile(filename, dimension)

    product = strassens(a, b, crossover=128)

    for i in range(dimension):
        print(product[i][i])

    print("\n")
