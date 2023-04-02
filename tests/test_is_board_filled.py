import pytest
from TicTacToe import TicTacToe


@pytest.fixture
def game():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.create_board()
    return tic_tac_toe


def test_is_board_filled(game):
    game.board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'X'],
        ['O', 'X', 'O']
    ]
    assert game.is_board_filled() == True

    game.board = [
        ['X', '-', 'X'],
        ['X', 'O', 'X'],
        ['O', 'X', 'O']
    ]
    assert game.is_board_filled() == False