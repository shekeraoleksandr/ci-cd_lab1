import random
from TicTacToe import TicTacToe


def test_get_random_first_player(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 0)
    tic_tac_toe = TicTacToe()
    assert tic_tac_toe.get_random_first_player() == 0

    monkeypatch.setattr(random, 'randint', lambda a, b: 1)
    tic_tac_toe = TicTacToe()
    assert tic_tac_toe.get_random_first_player() == 1
