import unittest
from main.Game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_initialization(self):
        self.assertEqual(self.game.current_player, 'X')
        self.assertEqual(self.game.status, 'ongoing')

    def test_switch_player(self):
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')

    def test_make_move_valid(self):
        result = self.game.make_move(0, 0)
        self.assertIn("Player O's turn", result)

    def test_make_move_invalid(self):
        self.game.make_move(0, 0)
        with self.assertRaises(ValueError):
            self.game.make_move(0, 0)

    def test_win_condition(self):
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 0)  # O
        self.game.make_move(0, 1)  # X
        self.game.make_move(1, 1)  # O
        result = self.game.make_move(0, 2)  # X wins
        self.assertIn("Player X wins!", result)

    def test_tie_condition(self):
        moves = [
            (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
            (1, 0, 'X'), (1, 1, 'X'), (1, 2, 'O'),
            (2, 0, 'O'), (2, 1, 'X'), (2, 2, 'O')
        ]
        for row, col, player in moves:
            if self.game.current_player != player:
                self.game.switch_player()
            self.game.make_move(row, col)
        self.assertEqual(self.game.status, 'tie')

if __name__ == '__main__':
    unittest.main()
