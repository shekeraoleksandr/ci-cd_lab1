import random


class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()

