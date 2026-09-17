# Модули и библиотека

# Импорт всей библиотеки
import math

# Импорт всей библиотеки через псевдоним
import math as m

# Импорт одной команды
from math import floor

# Импорт одной команды через псевдоним
from math import floor as f

# Импорт нескольких команд
from math import log2, log10

# Импорт нескольких команд через псевдоним
from math import log2 as l2, log10 as l10

# Импорт всех команд
from math import *

num = 10.5
print(math.ceil(num)) # Округление в большую сторону
print(floor(num)) # Округление в меньшую сторону
print(log2(16))
print(log10(100))