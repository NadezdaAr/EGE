from math import log2, ceil

N = 10 + 52 + 963
i = ceil(log2(N))
for L in range(1, 10000):
    I = ceil(L * i / 8)
    if I * 2000 <= 693 * 2 ** 10:
        print(L)