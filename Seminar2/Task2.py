num = int(input('Введите число: '))
f = 1
list = []
for i in range(1, num + 1):
    if i == 1:
        f = i
    else:                       
        f *= i
        i -= 1           
    list.append((f))
print(f'Произведение чисел от 1 до {num}: {list}')
