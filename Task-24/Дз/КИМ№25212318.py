with open (r'..\files\24_1866.txt') as file:
    data = file.readlines()
cnt = 1
ans = 0
for i in range(len(data) - 1):
    if data[i] + data[i+1] == 'ad':
        cnt = 1
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)