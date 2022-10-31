# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

coff = []
k = int(input('степень многочлена: '))

for i in range(k+1):
    num = randint(-10, 10)
    coff.append(num)

result = ''
for i in range(len(coff)):
    if len(result) > 0 and coff[i] > 0:
        result = result + ' + '
    if coff[i] == 0:
        continue
    result = result + str(coff[i]) + 'x^' + str(k - i)

if coff[-1] != 0:
    result = result[:len(result) - 3]

result = result + ' = 0'
print(result)

with open('file.txt', 'w') as f:
    f.write(result)
    