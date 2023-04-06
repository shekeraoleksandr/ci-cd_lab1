def test_show_board(capsys, game):
    game.board = [
        ['X', '-', 'O'],
        ['-', 'X', '-'],
        ['O', '-', 'X']
    ]
    game.show_board()
    captured = capsys.readouterr()
    assert captured.out == "X - O \n- X - \nO - X \n"
