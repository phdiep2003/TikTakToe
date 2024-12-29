import unittest
from main.Board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)

    def test_board_initialization(self):
        self.assertEqual(len(self.board.grid), 3)
        self.assertEqual(len(self.board.grid[0]), 3)
        self.assertTrue(all(cell is None for row in self.board.grid for cell in row))

    def test_make_move(self):
        self.board.make_move(0, 0, 'X')
        self.assertEqual(self.board.grid[0][0], 'X')

    def test_make_move_invalid(self):
        self.board.make_move(0, 0, 'X')
        with self.assertRaises(ValueError):
            self.board.make_move(0, 0, 'O')

    def test_is_full(self):
        for i in range(3):
            for j in range(3):
                self.board.make_move(i, j, 'X')
        self.assertTrue(self.board.is_full())

    def test_is_not_full(self):
        self.board.make_move(0, 0, 'X')
        self.assertFalse(self.board.is_full())

if __name__ == '__main__':
    unittest.main()
