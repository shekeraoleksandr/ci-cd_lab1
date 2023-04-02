import pytest
from TicTacToe import TicTacToe


@pytest.fixture
def game():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.create_board()
    return tic_tac_toe


def test_swap_player_turn(game):
    assert game.swap_player_turn('X') == 'O'
    assert game.swap_player_turn('O') == 'X'