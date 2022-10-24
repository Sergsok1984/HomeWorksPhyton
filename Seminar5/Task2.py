# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?


from random import randint

def input_dat(name):
    x = int(input(f"{name}, сколько конфет забираете (от 1 до 28)?: "))
    while x < 1 or x > 28:
        x = int(input('Введите корректное количество конфет от 1 до 28: '))
    return x


def p_print(name, k, count, value):
    print(f"{name} взял {k} конфет, итого у него {count} конфет. На столе осталось {value} конфет.")


print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. За один ход можно забрать не более, чем 28 конфет.')
player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(2021)
flag = randint(0, 1)
if flag:
    print(f"Первый ходит {player1}.")
else:
    print(f"Первый ходит {player2}.")

count1 = 0
count2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)              
        count1 += k 
        value -= k
        flag = False
        p_print(player1, k, count1, value)
    else: 
        k = input_dat(player2)                        
        count2 += k
        value -= k
        flag = True
        p_print(player2, k, count2, value)

if flag:
    print(f"Выиграл {player1}.")
else:
    print(f"Выиграл {player2}.")
