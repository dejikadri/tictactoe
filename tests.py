import unittest
import app_helper as hlp

class TestHelperFuncs(unittest.TestCase):
    def test_if_board_full(self):
        board = 'oooxxoxo'
        is_board_full = hlp.check_full_board(board)

        self.assertEquals(is_board_full, True)


    def test_if_board_not_full(self):
        board = 'oooxxoxo '
        is_board_full = hlp.check_full_board(board)

        self.assertEquals(is_board_full, False)
