lst = list(map(float, input("Введите числа через пробел:\n").split()))
lst2 = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(lst2) - min(lst2))
