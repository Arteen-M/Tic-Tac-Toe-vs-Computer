import Tic_Tac_Toe_COM
import time


def check_for_win(board_state):
    check = []
    for x in range(0, 3):
        for y in range(0, 3):
            check.append(board_state[x][y])
        if check.count("X") == 3:
            return 1
        elif check.count("O") == 3:
            return 2

        check = []

    for x in range(0, 3):
        for y in range(0, 3):
            check.append(board_state[y][x])
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


COM = Tic_Tac_Toe_COM.COM([['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']])

while True:
    # SETUP
    board = [['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']]
    print('', board[0], '\n', board[1], '\n', board[2])
    turn = 1
    p1 = []
    p2 = []

    # GAME LOOP
    while True:
        p1 = []
        p2 = []
        if turn == 1:
            print("Enter the X, then Y coordinates")
            p1 = [int(input()) for x in range(0, 2)]
            p1 = [p1[1], p1[0]]

            if board[p1[0]-1][p1[1]-1] == "N":
                board[p1[0]-1][p1[1]-1] = "X"
                turn = 2
            else:
                print("Square is already taken, try again")

        elif turn == 2:
            COM.update_board(board)
            p2 = COM.find_move()

            if board[p2[0]][p2[1]] == "N":
                board[p2[0]][p2[1]] = "O"
                turn = 1
            else:
                print("Square is already taken, try again")

            print('', board[0], '\n', board[1], '\n', board[2])

        if check_for_win(board) is not None:
            if check_for_win(board) > 0:
                print("PLAYER %d WINS!" % check_for_win(board))
                time.sleep(1)
                break
