ans = []

for num in range(41):
    lol = f'{num:b}'[-4:]
    if lol == '1011': ans.append(num)

print(ans)