import pytest
from TicTacToe import TicTacToe


@pytest.fixture
def game():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.create_board()
    return tic_tac_toe


def test_fix_spot(game):
    game.fix_spot(0, 0, 'X')
    assert game.board[0][0] == 'X'
