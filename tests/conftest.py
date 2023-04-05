import pytest
from TicTacToe import TicTacToe

#test config fixture
@pytest.fixture
def game():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.create_board()
    return tic_tac_toe
