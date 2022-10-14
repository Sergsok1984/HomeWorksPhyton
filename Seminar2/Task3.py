n = int(input('Введите n: '))
list = [((1 + 1 / i) ** i) for i in range(1, n + 1)]
print(sum(list))
