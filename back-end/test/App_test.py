import unittest
import json
from main.App import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_create_game(self):
        response = self.client.post('/create-game', json={'rows': 3, 'cols': 3, 'win_condition': 3})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('game_id', data)
        self.assertEqual(data['rows'], 3)
        self.assertEqual(data['cols'], 3)

    def test_make_move_valid(self):
        create_response = self.client.post('/create-game', json={'rows': 3, 'cols': 3, 'win_condition': 3})
        game_id = json.loads(create_response.data)['game_id']

        move_response = self.client.post('/make-move', json={'game_id': game_id, 'row': 0, 'col': 0})
        self.assertEqual(move_response.status_code, 200)
        self.assertIn("Player O's turn", json.loads(move_response.data)['message'])

    def test_make_move_invalid(self):
        create_response = self.client.post('/create-game', json={'rows': 3, 'cols': 3, 'win_condition': 3})
        game_id = json.loads(create_response.data)['game_id']

        self.client.post('/make-move', json={'game_id': game_id, 'row': 0, 'col': 0})
        move_response = self.client.post('/make-move', json={'game_id': game_id, 'row': 0, 'col': 0})

        self.assertEqual(move_response.status_code, 400)
        self.assertIn("Cell already taken", json.loads(move_response.data)['error'])

    def test_game_state(self):
        create_response = self.client.post('/create-game', json={'rows': 3, 'cols': 3, 'win_condition': 3})
        game_id = json.loads(create_response.data)['game_id']

        state_response = self.client.get(f'/game-state/{game_id}')
        self.assertEqual(state_response.status_code, 200)
        data = json.loads(state_response.data)
        self.assertEqual(data['current_player'], 'X')
        self.assertEqual(data['status'], 'ongoing')

if __name__ == '__main__':
    unittest.main()
