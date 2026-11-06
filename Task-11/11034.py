from math import *


for N in range(1, 10_000):
    i = ceil(log2(N))
    I = ceil(248 * i / 8)
    if I * 75_600 > 16 * 2 ** 20:
        print(N)
        break
