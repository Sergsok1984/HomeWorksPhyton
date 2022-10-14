from random import randint

n = int(input('Введите число элементов в списке: '))
lst = [randint(-n, n) for i in range(n)]
print(f'Заданный список:\n{lst}')
lst2 = []
f = open('Seminar2/file.txt', 'r')
for line in f.readlines():
    lst2.append(int(line))
f.close()
print(f'Список индексов:\n{lst2}')
prod = 1
for i in range(len(lst2)):
    if lst2[i] < len(lst):
        index = lst2[i]
        prod *= lst[index]
print(f'Произведение элементов заданного списка: {prod}')