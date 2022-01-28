import Tic_Tac_Toe_COM
import pygame
import sys

pygame.init()
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

HEIGHT = 300
WIDTH = HEIGHT

display = pygame.display.set_mode((WIDTH, HEIGHT))

board = [['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']]
COM = Tic_Tac_Toe_COM.COM(board)
cpu_play = False
end_game = False

tile_positions = [(0, 0, WIDTH / 3, HEIGHT / 3),
                  (WIDTH / 3, 0, WIDTH * 2 / 3, HEIGHT / 3),
                  (WIDTH * 2 / 3, 0, WIDTH, HEIGHT / 3),
                  (0, HEIGHT / 3, WIDTH / 3, HEIGHT * 2 / 3),
                  (WIDTH / 3, HEIGHT / 3, WIDTH * 2 / 3, HEIGHT * 2 / 3),
                  (WIDTH * 2 / 3, HEIGHT / 3, WIDTH, HEIGHT * 2 / 3),
                  (0, HEIGHT * 2 / 3, WIDTH / 3, HEIGHT),
                  (WIDTH / 3, HEIGHT * 2 / 3, WIDTH * 2 / 3, HEIGHT),
                  (WIDTH * 2 / 3, HEIGHT * 2 / 3, WIDTH, HEIGHT)]
board_colours = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]


def check_for_win(board_state):
    check = []
    for a in range(0, 3):
        for b in range(0, 3):
            check.append(board_state[a][b])
        if check.count("X") == 3:
            return 1
        elif check.count("O") == 3:
            return 2

        check = []

    for a in range(0, 3):
        for b in range(0, 3):
            check.append(board_state[b][a])
        if check.count("X") == 3:
            return 1
        elif check.count("O") == 3:
            return 2

        check = []

    check = [board_state[0][0], board_state[1][1], board_state[2][2]]

    if check.count("X") == 3:
        return 1
    elif check.count("O") == 3:
        return 2

    check = [board_state[0][2], board_state[1][1], board_state[2][0]]

    # Check the second combination for corners

    if check.count("X") == 3:
        return 1
    elif check.count("O") == 3:
        return 2


def button(x, y, w, h, board_pos, board_state):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if w > mouse[0] > x and h > mouse[1] > y:
        if click[0] == 1 and board_state[board_pos[0]][board_pos[1]] == 'N':
            return board_pos


def win_loss_check(board_state):
    count = 0
    if check_for_win(board_state) is not None:
        return check_for_win(board_state)
    else:
        for a in range(len(board_state)):
            for b in range(len(board_state)):
                if board_state[a][b] == "N":
                    count += 1

        if count == 0:
            return 0


while True:

    board = [['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']]
    board_colours = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
    cpu_play = False
    end_game = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        COM.update_board(board)

        for x in range(0, 3):
            for y in range(0, 3):
                if board[x][y] == 'X' and board_colours[(x*3)+y] == BLACK:
                    board_colours[(x * 3) + y] = RED

                    if win_loss_check(board) is not None:
                        end_game = True
                    else:
                        cpu_play = True

                elif board[x][y] == 'O' and board_colours[(x*3)+y] == BLACK:
                    board_colours[(x * 3) + y] = BLUE

                    if win_loss_check(board) is not None:
                        end_game = True
                    else:
                        cpu_play = False

        for x in range(0, len(board_colours)):
            pygame.draw.rect(display, board_colours[x], tile_positions[x])

        if cpu_play:
            p2 = COM.find_move()

            try:
                if board[p2[0]][p2[1]] == "N":
                    board[p2[0]][p2[1]] = "O"
                else:
                    print("Square is already taken, try again")
            except TypeError:
                pass

        pygame.draw.line(display, (100, 100, 100), (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 10)
        pygame.draw.line(display, (100, 100, 100), (WIDTH * 2 / 3, 0), (WIDTH * 2 / 3, HEIGHT), 10)

        pygame.draw.line(display, (100, 100, 100), (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 10)
        pygame.draw.line(display, (100, 100, 100), (0, HEIGHT * 2 / 3), (WIDTH, HEIGHT * 2 / 3), 10)

        buttons = [button(0, 0, WIDTH / 3, HEIGHT / 3, [0, 0], board),  # 0, 0
                   button(WIDTH / 3, 0, WIDTH * 2 / 3, HEIGHT / 3, [0, 1], board),  # 0, 1
                   button(WIDTH * 2 / 3, 0, WIDTH, HEIGHT / 3, [0, 2], board),  # 0, 2
                   button(0, HEIGHT / 3, WIDTH / 3, HEIGHT * 2 / 3, [1, 0], board),  # 1, 0
                   button(WIDTH / 3, HEIGHT / 3, WIDTH * 2 / 3, HEIGHT * 2 / 3, [1, 1], board),  # 1, 1
                   button(WIDTH * 2 / 3, HEIGHT / 3, WIDTH, HEIGHT * 2 / 3, [1, 2], board),  # 1, 2
                   button(0, HEIGHT * 2 / 3, WIDTH / 3, HEIGHT, [2, 0], board),  # 2, 0
                   button(WIDTH / 3, HEIGHT * 2 / 3, WIDTH * 2 / 3, HEIGHT, [2, 1], board),  # 2, 1
                   button(WIDTH * 2 / 3, HEIGHT * 2 / 3, WIDTH, HEIGHT, [2, 2], board)]  # 2, 2

        if buttons[0] is not None:
            board[buttons[0][0]][buttons[0][1]] = "X"
        elif buttons[1] is not None:
            board[buttons[1][0]][buttons[1][1]] = "X"
        elif buttons[2] is not None:
            board[buttons[2][0]][buttons[2][1]] = "X"
        elif buttons[3] is not None:
            board[buttons[3][0]][buttons[3][1]] = "X"
        elif buttons[4] is not None:
            board[buttons[4][0]][buttons[4][1]] = "X"
        elif buttons[5] is not None:
            board[buttons[5][0]][buttons[5][1]] = "X"
        elif buttons[6] is not None:
            board[buttons[6][0]][buttons[6][1]] = "X"
        elif buttons[7] is not None:
            board[buttons[7][0]][buttons[7][1]] = "X"
        elif buttons[8] is not None:
            board[buttons[8][0]][buttons[8][1]] = "X"

        pygame.display.update()

        if end_game:
            if win_loss_check(board) == 0:
                print("TIE")
            elif win_loss_check(board) > 0:
                print("PLAYER %d WINS!" % win_loss_check(board))
            pygame.time.delay(5000)
            break

        pygame.time.delay(10)
