def test_show_board(capfd, game):
    game.board = [
        ['X', '-', 'O'],
        ['-', 'X', '-'],
        ['O', '-', 'X']
    ]
    game.show_board()
    captured = capfd.readouterr()
    assert captured.out == "X - O \n- X - \nO - X \n"
