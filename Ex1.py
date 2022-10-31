# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}

from math import pi
from random import randint

d = randint(1, 15)
print(f'число π с точностью в {d} знака(ов) = {round(pi, d)}')