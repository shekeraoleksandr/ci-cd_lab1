def test_is_player_win(game):
    game.board = [
        ['O', 'O', 'O'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    assert game.is_player_win('O')

    game.board = [
        ['X', '-', '-'],
        ['X', '-', '-'],
        ['X', '-', '-']
    ]
    assert game.is_player_win('X')

    game.board = [
        ['X', '-', '-'],
        ['-', 'X', '-'],
        ['-', '-', 'X']
    ]
    assert game.is_player_win('X')

    game.board = [
        ['X', '-', 'O'],
        ['O', 'O', 'X'],
        ['X', 'O', '-']
    ]
    assert not game.is_player_win('O')
