from strassencl import *
from random import randint
import sys
from datetime import datetime

start = int(sys.argv[1])
end = int(sys.argv[2])

a = [[randint(-1, 1) for j in range(end)] for i in range(end + 1)]
b = [[randint(-1, 1) for j in range(end)] for i in range(end + 1)]

splits = [ceil(end/2**i) for i in range(1, ceil(log(end,2)))]
print(splits)
for c in splits:

    t_start = datetime.now()
    strassens(a, b, crossover = c)
    t = datetime.now() - t_start

    print(c, t)
