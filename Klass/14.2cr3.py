from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num = 283 ** 382 + 9 ** 15 + 2 ** 3
num = convert(num, 14)

print(num.count('b') - num.count('c'))
