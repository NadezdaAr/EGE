# Псевдослучайные числа
from random import *

print(randint(1, 100)) # Целое число от а до b
print(uniform(1,100)) # Дробное число от а до b
print(random()) # Дробное число от 0 до 1

data = ['Vova', 'Boris', 'Julia']
print(choice(data))
print(choices(data, k=2))
print(sample(data, k=2))
(shuffle(data))
print(data)

#abs - модуль числа