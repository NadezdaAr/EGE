num1 = 41
num2 = 131
stp = 3
cnt = 0
while num1:
    if num1 % stp == stp: cnt +=1
    num //= 5
print(cnt)

def convert(num, sys):
    res = ''
    while num:
        res+= str(num % sys)
        num //= sys
    return res[::-1] if res else '0'
