# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

lst1 = [int(i) for i in input("Введите числа через пробел:\n").split()]
lst2, lst3 = [], []
for i in set(lst1):
    if lst1.count(i) > 1:
        lst3.append(i)
    else: 
        lst2.append(i) 
print(f"Заданный список: {lst1}\n"
      f"Список неповторяющихся элементов: {lst2}\n"
      f"Список дубликатов: {lst3}\n"
      f"Список без дубликатов: {list(set(lst1))}")