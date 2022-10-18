n = int(input('Введите число: '))
fib_lst = []
fib1, fib2 = 0, 1
for i in range(n):
    fib1, fib2 = fib2, fib1 + fib2
    fib_lst.append(fib1)
fib_lst2 = fib_lst[::-1]
if n % 2 == 0: 
    for i in range(len(fib_lst2)):
        if i % 2 == 0:
           fib_lst2[i] *= - 1
else: 
    for i in range(len(fib_lst2)):
        if i % 2 != 0:
           fib_lst2[i] *= - 1
fib_lst2.extend(fib_lst)
print(f'Список чисел Фибоначчи, в т.ч. для отрицательных индексов:\n', fib_lst2)
