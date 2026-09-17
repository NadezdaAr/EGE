# Функции

def error_alert(message):
    print('Error' + message)

def sum_of_digits(num):
    summ = 0
    while num:
        summ += num % 10
        num //= 10
    return summ

print(sum_of_digits(123))