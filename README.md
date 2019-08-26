# GameOfLive
python implementation of Game of Live a simple game in a 2D Map board, the board is composed of cells which have a state the porpuse of the game is to find the next board state give the criterias below:

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.



The  python version has been written following TDD (Test Driven Developmet) where the test has been designed before the implemntation, to see which test has been considered see test_cell.py and test_game.py

to run all tst cases run as 'python -m unittest'


