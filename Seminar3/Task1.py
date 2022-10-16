from random import randint

n = int(input('Введите число элементов в списке: '))
lst = [randint(-100, 100) for i in range(n)]
print(f'Заданный список:\n{lst}')
sum = 0
for i in range(1, len(lst), 2):
    sum += lst[i]
print(f'Сумма элементов на нечетных позициях:', sum)
