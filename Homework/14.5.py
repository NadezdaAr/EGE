from string import printable as alph

num = 4**36 + 3 * 4**20 + 4**15 + 2 * 4**7 + 49

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

print(set(convert(num, 16)))