# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

from random import randint

num = randint(4, 100)
print(f'для числа {num} простые множители:')
i = 2
lst = []
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(lst)