from main.Board import Board

class Game:
    def __init__(self, rows=3, cols=3, win_condition=3):
        self.board = Board(rows, cols)
        self.players = ['X', 'O']
        self.current_player = 'X'
        self.win_condition = win_condition
        self.status = 'ongoing'  # 'ongoing', 'win', 'tie'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self, symbol):
        directions = [
            (0, 1),  # Horizontal
            (1, 0),  # Vertical
            (1, 1),  # Diagonal \
            (1, -1)  # Diagonal /
        ]

        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board.grid[row][col] != symbol:
                    continue

                for dx, dy in directions:
                    count = 1
                    for step in range(1, self.win_condition):
                        x, y = row + dx * step, col + dy * step
                        if 0 <= x < self.board.rows and 0 <= y < self.board.cols and self.board.grid[x][y] == symbol:
                            count += 1
                        else:
                            break

                    if count == self.win_condition:
                        return True
        return False

    def make_move(self, row, col):
        if self.status != 'ongoing':
            raise ValueError("Game is already over")

        self.board.make_move(row, col, self.current_player)

        if self.check_win(self.current_player):
            self.status = 'win'
            return f"Player {self.current_player} wins!"

        if self.board.is_full():
            self.status = 'tie'
            return "The game is a tie!"

        self.switch_player()
        return f"Player {self.current_player}'s turn"

    def get_state(self):
        return {
            'board': self.board.get_state(),
            'current_player': self.current_player,
            'status': self.status
        }
