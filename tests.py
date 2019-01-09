import unittest
import app_helper as hlp

class TestHelperFuncs(unittest.TestCase):
    def test_if_board_full(self):
        board = 'oooxxoxo'
        is_board_full = hlp.check_full_board(board)

        self.assertEqual(is_board_full, True)


    def test_if_board_not_full(self):
        board = 'oooxxoxo '
        is_board_full = hlp.check_full_board(board)
        self.assertEqual(is_board_full, False)

    def test_for_winner_o(self):
        board = 'oooxxoxxo'
        is_winner = hlp.check_winning_player(board)
        self.assertEqual(is_winner, 'o wins')


    def test_for_winner_x(self):
        board = 'ooxxxoxxx'
        is_winner = hlp.check_winning_player(board)
        self.assertEqual(is_winner, 'x wins')

    def test_for_winner(self):
        board = 'oox' \
                'oxo' \
                'xxo'
        is_winner = hlp.check_winner(board, 'x')
        self.assertEqual(is_winner, True)

    def test_api_move(self):
        board = 'ooxxxoxx '
        new_board = hlp.change_xter(board, 8, 'o')
        self.assertEqual(new_board, 'ooxxxoxxo')

    def test_board_position_empty(self):
        board = 'ooxxxoxx '
        self.assertEqual(hlp.is_position_empty(board, 8), True)
        self.assertEqual(hlp.is_position_empty(board, 7), False)