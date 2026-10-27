ans = []
for N in range(1,10_000):
    R = f"{N:b}"
    if R[-1] == "0":
        R = "10" + R
    else:
        R = "1" + R + "1"
    R = int(R, 2)
    if R > 441:
        ans.append(N)
        ans = ans + [N] # [1, 2, 3] + N
print(min(ans))