# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Введите натуральную степень k = "))
lst = [random.randint(0, 100) for i in range(k + 1)]
lst = lst[::-1]
polynom = ''
if len(lst) < 1: 
    polynom = 'x = 0' 
else: 
    for i in range(len(lst)):
        if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
            polynom += f'{lst[i]}x^{len(lst)-i-1}'
            if lst[i+1] != 0:
                polynom += ' + '
        elif i == len(lst) - 2 and lst[i] != 0:
            polynom += f'{lst[i]}x'
            if lst[i+1] != 0:
                polynom += ' + '
        elif i == len(lst) - 1 and lst[i] != 0:
            polynom += f'{lst[i]} = 0'
        elif i == len(lst) - 1 and lst[i] == 0:
            polynom += ' = 0'

with open('Seminar4/polynom.txt', 'w') as data:
        data.write(polynom)
print(polynom)


