import pytest
from TicTacToe import TicTacToe


@pytest.fixture
def game():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.create_board()
    return tic_tac_toe


def test_create_board(game):
    assert len(game.board) == 3
    assert all(len(row) == 3 for row in game.board)
    assert all(item == '-' for row in game.board for item in row)
