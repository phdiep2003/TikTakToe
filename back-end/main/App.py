from flask import Flask, request, jsonify
from main.Game import Game

app = Flask(__name__)

# Store games in memory
games = {}

@app.route('/create-game', methods=['POST'])
def create_game():
    data = request.json
    rows = data.get('rows', 3)
    cols = data.get('cols', 3)
    win_condition = data.get('win_condition', 3)

    game = Game(rows, cols, win_condition)
    game_id = len(games) + 1
    games[game_id] = game

    return jsonify({'game_id': game_id, 'rows': rows, 'cols': cols, 'win_condition': win_condition}), 201

@app.route('/make-move', methods=['POST'])
def make_move():
    data = request.json
    game_id = data.get('game_id')
    row = data.get('row')
    col = data.get('col')

    game = games.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404

    try:
        result = game.make_move(row, col)
        return jsonify({'message': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/game-state/<int:game_id>', methods=['GET'])
def game_state(game_id):
    game = games.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404

    return jsonify(game.get_state())

if __name__ == '__main__':
    app.run(debug=True)
