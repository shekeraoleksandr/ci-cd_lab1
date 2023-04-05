def test_swap_player_turn(game):
    assert game.swap_player_turn('X') == 'O'
    assert game.swap_player_turn('O') == 'X'
