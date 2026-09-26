with open(r"..\files\24_2942.txt") as file:
    data = file.readlines()

data = "**ABACACB***ABACAB***AB***"

ans = cnt = i = 0
len_data = len(data) - 1
while i < len_data:
    if data[i] + data[i + 1] in "AB AC": #или if data[i:i +2], тогда к лен дата пишем - 1
        cnt +=1
        i +=2
        ans = max(ans, cnt)
    else:
        cnt = 0
        i +=1

print(ans)