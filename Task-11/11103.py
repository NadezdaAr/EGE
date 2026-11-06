from math import log2, ceil

for L in range(1, 10000):
    N = 70 + 10
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 1234567 * I > 24 * 2 ** 20:
        print(L)
        break