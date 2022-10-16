num = int(input('Введите десятичное число: '))
binary_num = ''
while num > 0:
    binary_num = str(num % 2) + binary_num
    num //= 2    
print(f'Число в двоичной СС:', binary_num)
