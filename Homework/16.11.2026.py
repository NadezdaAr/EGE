from string import printable as alph
ans = []
for x in alph[:27]:
    num1 = int(f'8{x}38{x}68', 27)
    num2 = int(f'37{x}3163', 27)
    num = num1 + num2
    if num % 26 == 0:
        print(num // 26)

##########################################
from string import printable as alph
ans = []
for x in alph[:16]:
    num1 = int(f'11{x}73', 16)
    num2 = int(f'94662{x}53{x}', 16)
    num3 = int(f'6{x}41', 16)
    num4 = int(f'31{x}77', 16)
    num5 = int(f'9{x}82{x}{x}181', 16)
    num = num1 + num2 + num3 + num4 + num5
    if num % 15 == 0:
        print(num // 15)
###########################################
from string import printable as alph
ans = []
for x in alph[:13]:
    num1 = int(f'9{x}AB', 13)
    num2 = int(f'{x}46C', 16)
    num3 = int(f'B7{x}', 15)
    num = num1 + num2 - num3
    if num % 14 == 0:
        print(num // 14)
###########################################
from string import printable as alph
ans = []
for x in range(16, 37):
    num1 = int('17496', x)
    num2 = int('91F83', x)
    num3 = int('D9543', x)
    num = num1 + num2 + num3
    if num % 12 == 0:
        print(x, num // 12)
###########################################