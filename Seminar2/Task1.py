number = input('Введите число: ')
sum = 0
for num in number:
    if num.isdigit():
        sum += int(num)
print('Сумма цифр:', sum)
