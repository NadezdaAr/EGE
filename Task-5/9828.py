from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys) #res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'
