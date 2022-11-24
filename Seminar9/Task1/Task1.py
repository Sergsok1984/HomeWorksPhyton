import pygame

pygame.init()

green = (0, 200, 64)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)


def draw_board(screen):
    pygame.draw.line(screen, black, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, black, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, black, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, black, (0, 200), (300, 200), 3)


def make_move(screen, symbol):
    for i in range(3):
        for j in range(3):
            if symbol[i][j] == "0":
                pygame.draw.circle(screen, (blue),
                                   (j * 100 + 50, i * 100 + 50), 45, 10)
            elif symbol[i][j] == "x":
                pygame.draw.line(screen, (green), (j * 100 + 5,
                                 i * 100 + 5), (j * 100 + 95, i * 100 + 95), 20)
                pygame.draw.line(screen, (green), (j * 100 +
                                 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 20)


def win_combination(board, symbol):
    if_win = False
    for line in board:
        if line.count(symbol) == 3:
            if_win = True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            if_win = True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        if_win = True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        if_win = True
    return if_win


SCREEN_SIZE = (300, 300)

window = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.Surface(SCREEN_SIZE)

pygame.display.set_caption("КРЕСТИКИ-НОЛИКИ")
screen.fill((white))

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

runGame = True
move = 1
game_over = False

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if board[pos[1] // 100][pos[0] // 100] == "" and move % 2 != 0:
                board[pos[1] // 100][pos[0] // 100] = "x"
                move += 1
            if board[pos[1] // 100][pos[0] // 100] == "" and move % 2 == 0:
                board[pos[1] // 100][pos[0] // 100] = "0"
                move += 1

            player_1 = win_combination(board, "x")
            player_2 = win_combination(board, "0")

            if player_1 or player_2:
                game_over = True
                if player_1:
                    pygame.display.set_caption("Победили крестики!")
                else:
                    pygame.display.set_caption("Победили нолики!")
            elif move == 10 and not game_over:
                game_over = True
                pygame.display.set_caption("Ничья!!!")                     

    make_move(screen, board)
    draw_board(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()