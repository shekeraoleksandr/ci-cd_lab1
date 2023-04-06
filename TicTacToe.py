import random

import char as char


class TicTacToe:

    def __init__(self):
        self.board = []
        self.n = 3

    def create_board(self):
        '''
        this method creates an empty board filled with -
        :return:
        full board
        '''
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        '''
        this method chooses a player which turn It is on random
        :return:
        random player id
        '''
        return random.randint(0, 1)

    def fix_spot(self, row: int, col: int, player: chr):
        '''
        this method is used to fix spot a player's chosen location
        :return:
        chosen position into array
        '''
        self.board[row][col] = player

    def is_player_win(self, player: chr):
        '''
        this method finds out whether the player meets the win condition
        :return:
        win=false/true
        '''
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        '''
        this finds out whether the board is filled resulting in a draw
        :return:
        full true if yes,false if no
        '''
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player: chr):
        '''
        this swaps the player's turn
        :return:
        player's index (x or 0)
        '''
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        '''
        this is used to show the board created with create_board
        :return:
        create_board
        '''
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        '''
        this is the main function
        :return:
        final view of the board
        '''
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
