day = int(input('Введите день недели от 1 до 7: '))
if 6 <= day <= 7: 
    print('да')
elif 1 <= day <= 5: 
    print('нет')
else: 
    print('Введено некорректное число')
