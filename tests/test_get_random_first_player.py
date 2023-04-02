import pytest
import random
from TicTacToe import TicTacToe
@pytest.fixture
def game():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.create_board()
    return tic_tac_toe
def test_get_random_first_player(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 0)
    tic_tac_toe = TicTacToe()
    assert tic_tac_toe.get_random_first_player() == 'O'

    monkeypatch.setattr(random, 'randint', lambda a, b: 1)
    tic_tac_toe = TicTacToe()
    assert tic_tac_toe.get_random_first_player() == 'X'