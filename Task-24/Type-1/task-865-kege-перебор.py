with open(r"..\files\kfdhsukfh") as file:
    data = file.readlines()

cnt = ans = 0

for i in range(len(data)):
    if data[i]  == 'C' or data[i]  == 'F': # if data[i] in 'CF':
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)

print(ans)