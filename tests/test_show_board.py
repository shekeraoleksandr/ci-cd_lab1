import pytest
from TicTacToe import TicTacToe
@pytest.fixture
def game():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.create_board()
    return tic_tac_toe
def test_show_board(capfd, game):
    game.board = [
        ['X', '-', 'O'],
        ['-', 'X', '-'],
        ['O', '-', 'X']
    ]
    game.show_board()
    captured = capfd.readouterr()
    assert captured.out == "X - O \n- X - \nO - X \n"