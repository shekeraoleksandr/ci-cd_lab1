import random


class TicTacToe:
    def __init__(self):
        self.board = []

    def get_random_first_player(self):
        return random.randint(0, 1)


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
