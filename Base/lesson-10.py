# Цикл while

# Нахождение суммы цифр числа любой длины

num = 56
summ = 0
while num:
    summ += num % 10
    num //= 10
print(summ)

# Цикл for

# range(n, m, k) - создает числовой диапазон от n до m с шагом k
print(*range(1, 5)) # от 1 до 5 не включительно
print(*range(10)) # от 0 до 10 не включительно
print(*range(4, 10, 2)) # от 4 до 10 не включительно с шагом 2

for i in range(15, 0, -3):
    print(i)

data = ['User1', 'User2', 'User3']
for i in data:
    print(i)

#################################################################
# Напишите программу, которая выводит на экран количество разрядов введенного пользователем числа.

def amount_of_digits(num):
    cnt = 0
    while num:
        cnt += 1
        num //= 10
    return cnt

