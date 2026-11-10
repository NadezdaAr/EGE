from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 10_000):
    R = convert(N, 3)
    if N % 2 == 0:
        R = R + R[-2:]
    else:
        R = R + convert(sum(map(int, R)), 3)
    R = int(R, 3)
    if n > 9:
        ans.append([R,N])
print(min(ans))
print(ans)