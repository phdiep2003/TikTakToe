class Board:  # Corrected syntax
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def make_move(self, row, col, symbol):
        if self.grid[row][col] is not None:
            raise ValueError("Cell already taken")
        self.grid[row][col] = symbol

    def is_full(self):
        return all(cell is not None for row in self.grid for cell in row)

    def get_state(self):
        return self.grid
