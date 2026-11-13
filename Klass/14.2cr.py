from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res [::-1] if res else '0'

ans = []

for N in range(1, 10_000):
    R = convert(N, 3)
    M = sum(map(int, R))
    if M % 3 == 0:
        R = R + '212'
    else:
        R += convert(M * 2, 3)
        R = int(R, 3)
        if R > 490:
            ans.append(R)
print(min(ans))