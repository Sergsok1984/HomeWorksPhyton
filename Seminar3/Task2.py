# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

n = int(input('Введите число элементов в списке: '))
lst = [randint(-10, 10) for i in range(n)]
print(f'Заданный список:\n', lst)
lst2 = []
if len(lst) % 2 == 0:
    for i in range(0, int(len(lst) / 2)):            
        a = lst[i] * lst[len(lst) - i - 1]        
        lst2.append(a)
else:
    for i in range(0, int(len(lst) / 2) + 1):            
        a = lst[i] * lst[len(lst) - i - 1]        
        lst2.append(a)
print(f'Результирующий список:\n', lst2)
