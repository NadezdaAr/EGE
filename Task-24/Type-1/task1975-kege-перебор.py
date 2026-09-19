with open(r'..\files\24_1975.txt') as file:
    data = file.readlines()

# file = open(r'..\files\24_1975.txt')
# data = file.readline()
# file.close()

cnt = 1
ans = 0
# или же cnt, ans = 1, 0 ( 1, 0 - это tuple)

# *args - звёздочка распаковывает элемент

for i in range(len(data) - 1):
    if data[i] + data[i+1] == "PP" or data[i:i +2] == 'PP' :
        cnt = 1
    else:
        cnt += 1
    ans = max(ans, cnt)

print(ans)