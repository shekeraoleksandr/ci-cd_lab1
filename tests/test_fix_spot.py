def test_fix_spot(game):
    game.fix_spot(0, 0, 'X')
    assert game.board[0][0] == 'X'
