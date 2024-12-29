# TikTakToe

Each game has 2 players and a board, each player has either X or O. Before the Game start, We can select the number of rows and columns of the Board (default n=3 for a 3x3 board) with corresponding winning conditions number of consecutive elements (defaults 3 on the same row, column or diagonal)

To run the test manually, you can
1. Go to back-end
```
cd back-end
```
2. Create a new python virtual environment
```
python -m venv newenv
```
```
source newenv/bin/activate
```
```
pip install Flask
```
4. Run all tests
```
python3 -m unittest discover -s test -p "*.py"
```
