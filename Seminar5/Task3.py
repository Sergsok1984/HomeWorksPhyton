# Создайте программу для игры в ""Крестики-нолики"".

table = list(range(1, 10))


def draw_table(table):
    print("-" * 13)
    for i in range(3):
        print("|", table[0 + i * 3], "|", table[1 + i * 3], "|", table[2 + i * 3], "|")
        print("-" * 13)


def move(X_or_0):
    valid = False
    while not valid:
        player_move= input("В какую клетку поставим " + X_or_0 + "? ")
        try:
            player_move = int(player_move)
        except:
            print("Некорректный ввод.")
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(table[player_move - 1]) not in "XO"):
                table[player_move - 1] = X_or_0
                valid = True
            else:
                print("Клетка занята")
        else:
            print("Некорректный ввод. Введите номер клетки от 1 до 9.")


def win_combination(table):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if table[each[0]] == table[each[1]] == table[each[2]]:
            return table[each[0]]
    return False


def game(table):
    counter = 0
    win = False
    while not win:
        draw_table(table)
        if counter % 2 == 0:
            move("X")
        else:
            move("O")
        counter += 1
        if counter > 4:
            tmp = win_combination(table)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_table(table)

game(table)
