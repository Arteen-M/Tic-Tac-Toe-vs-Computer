# THE COMPUTERS CLASS
class COM:
    # DEFINE THE BOARD
    def __init__(self, board_state):
        self.board = board_state

    # UPDATE THE BOARD
    def update_board(self, board_state):
        self.board = board_state

    # CHECK ROWS AND COLUMNS
    def check_row_column(self, win=True):
        # Look either for a potential win or loss (order matters)
        if win:
            winner = "O"
            loser = "X"
        else:
            winner = "X"
            loser = "O"

        check = [[], []]  # Puts three tiles in this list
        # ROW
        for x in range(0, 3):  # Used to check all three rows
            for y in range(0, 3):  # Check all three tiles in each row
                # Puts tile states and position in the check list
                check[0].append(self.board[x][y])
                check[1].append([x, y])
            # Check if two of the same tile are in the list, if so, return the position of the empty tile
            if check[0].count(winner) == 2 and check[0].count(loser) == 0:
                return check[1][check[0].index("N")]
            check = [[], []]

        # COLUMN (Same process as the row, just with X and Y flipped)
        for x in range(0, 3):
            for y in range(0, 3):
                check[0].append(self.board[y][x])
                check[1].append([y, x])
            if check[0].count(winner) == 2 and check[0].count(loser) == 0:
                return check[1][check[0].index("N")]
            check = [[], []]

    # CHECK THE CORNERS
    def check_corner(self, win=True):
        # Look either for a potential win or loss (order matters)
        if win:
            winner = "O"
            loser = "X"
        else:
            winner = "X"
            loser = "O"

        # Since there are only two pairs of winnable corners, brute forcing the win/loss check works fine
        # Appends two corners and the center to the list for the check
        check = [[self.board[0][0], self.board[1][1], self.board[2][2]], [[0, 0], [1, 1], [2, 2]]]

        if check[0].count(winner) == 2 and check[0].count(loser) == 0:
            return check[1][check[0].index("N")]

        # Check the second combination for corners
        check = [[self.board[0][2], self.board[1][1], self.board[2][0]], [[0, 2], [1, 1], [2, 0]]]

        if check[0].count(winner) == 2 and check[0].count(loser) == 0:
            return check[1][check[0].index("N")]

    # CHECK IF THE CENTER TILE IS AVAILABLE
    def center(self):
        if self.board[1][1] == "N":
            return [1, 1]

    # CHECK IF A CORNER OPPOSITE TO ONE OWNED BY THE OPPONENT IS AVAILABLE
    def opposite_corner(self):
        if self.board[0][0] != "N" and self.board[2][2] == "N":
            return [2, 2]
        elif self.board[0][2] != "N" and self.board[2][0] == "N":
            return [2, 0]
        elif self.board[2][0] != "N" and self.board[0][2] == "N":
            return [0, 2]
        elif self.board[2][2] != "N" and self.board[1][1] == "N":
            return [0, 0]

    # CHECK IF THERE IS AN EMPTY CORNER AVAILABLE
    def empty_corner(self):
        if self.board[0][0] == "N":
            return [0, 0]
        elif self.board[0][2] == "N":
            return [0, 2]
        elif self.board[2][0] == "N":
            return [2, 0]
        elif self.board[2][2] == "N":
            return [2, 2]

    # CHECK FOR EMPTY EDGES
    def empty_edge(self):
        if self.board[0][1] == "N":
            return [0, 1]
        elif self.board[1][0] == "N":
            return [1, 0]
        elif self.board[1][2] == "N":
            return [1, 2]
        elif self.board[2][1] == "N":
            return [2, 1]

    # PERFORM EACH CHECK IN ORDER OF IMPORTANCE
    def find_move(self):
        if self.check_row_column(True) is not None:
            return self.check_row_column(True)

        elif self.check_row_column(False) is not None:
            return self.check_row_column(False)

        elif self.check_corner(True) is not None:
            return self.check_corner(True)

        elif self.check_corner(False) is not None:
            return self.check_corner(False)

        elif self.center() is not None:
            return self.center()

        elif self.opposite_corner() is not None:
            return self.opposite_corner()

        elif self.empty_corner() is not None:
            return self.empty_corner()

        elif self.empty_edge is not None:
            return self.empty_edge()
