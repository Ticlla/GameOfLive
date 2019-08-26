import unittest
from game import Game
from cell import Cell


class GameTest(unittest.TestCase):

	# Test Inital Game board state
	def test_initialize_game_state(self):
		initial_game_state = [
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.DEATH,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE]
		]
		game = Game(initial_game_state)
		expected_game_state = [
		[Cell(Cell.ALIVE),Cell(Cell.ALIVE),Cell(Cell.ALIVE)],
		[Cell(Cell.ALIVE),Cell(Cell.DEATH),Cell(Cell.ALIVE)],
		[Cell(Cell.ALIVE),Cell(Cell.ALIVE),Cell(Cell.ALIVE)]
		]

		for i in range(len(initial_game_state)):
			for j in range(len(initial_game_state[0])):
				if initial_game_state[i][j] == 1:
					expected = 'o'
				else: 
					expected = '.'
				self.assertEqual(str(game.board[i][j]), expected)

	# Test retrieve specific cell on row, col
	def test_retrieve_cellstate_at_location(self):
		initial_game_state = [
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.DEATH,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE]
		]
		game = Game(initial_game_state)
		cell_location = game.getCell(0,0)
		self.assertEqual(Cell.ALIVE,cell_location.state)		
		cell_location = game.getCell(1,1)
		self.assertEqual(Cell.DEATH,cell_location.state)	

	# Test number of neighbours on happy path,it menans all memberer are live neighbours
	def test_number_of_neighbours_happy_path(self):
		initial_game_state = [
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE]
		]
		game = Game(initial_game_state)
		neighbours = game.getNumberNeighbours(1,1)
		expected_neighbours = 8
		self.assertEqual(expected_neighbours,neighbours)		
	
	# Test number of neighbours on the top corner  which means should not have all neigh boours
	def test_number_of_neighbours_top_corner(self):
		initial_game_state = [
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE]
		]
		game = Game(initial_game_state)
		neighbours = game.getNumberNeighbours(0,0)
		expected_neighbours = 3
		self.assertEqual(expected_neighbours,neighbours)		

		neighbours = game.getNumberNeighbours(0,2)
		expected_neighbours = 3
		self.assertEqual(expected_neighbours,neighbours)

	# Test number of neighbours on the bottom corner  which means should not have all neigh boours
	def test_number_of_neighbours_bottom_corner(self):
		initial_game_state = [
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE]
		]
		game = Game(initial_game_state)
		neighbours = game.getNumberNeighbours(2,0)
		expected_neighbours = 3
		self.assertEqual(expected_neighbours,neighbours)		

		neighbours = game.getNumberNeighbours(2,2)
		expected_neighbours = 3
		self.assertEqual(expected_neighbours,neighbours)

	# Test number of neighbours on the border  which means should not have all neigh boours
	def test_number_of_neighbours_border(self):
		initial_game_state = [
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE]
		]
		game = Game(initial_game_state)
		neighbours = game.getNumberNeighbours(0,1)
		expected_neighbours = 5
		self.assertEqual(expected_neighbours,neighbours)		

		neighbours = game.getNumberNeighbours(2,1)
		expected_neighbours = 5
		self.assertEqual(expected_neighbours,neighbours)

		game = Game(initial_game_state)
		neighbours = game.getNumberNeighbours(1,0)
		expected_neighbours = 5
		self.assertEqual(expected_neighbours,neighbours)		

		neighbours = game.getNumberNeighbours(1,2)
		expected_neighbours = 5
		self.assertEqual(expected_neighbours,neighbours)

	# Test The next game state on a single iteration of state
	def test_next_game_state(self):
		initial_game_state = [
		[Cell.DEATH,Cell.ALIVE,Cell.DEATH],
		[Cell.DEATH,Cell.ALIVE,Cell.DEATH],
		[Cell.DEATH,Cell.ALIVE,Cell.DEATH]
		]

		game = Game(initial_game_state)

		new_state = game.nextGameState()
		expected_game_state = [
		[Cell(Cell.DEATH),Cell(Cell.DEATH),Cell(Cell.DEATH)],
		[Cell(Cell.ALIVE),Cell(Cell.ALIVE),Cell(Cell.ALIVE)],
		[Cell(Cell.DEATH),Cell(Cell.DEATH),Cell(Cell.DEATH)]
		]

		for i in range(len(expected_game_state)):
			for j in range(len(expected_game_state[0])):
				if expected_game_state[i][j].state == 1:
					expected = 'o'
				else: 
					expected = '.'
				self.assertEqual(str(game.board[i][j]), expected)


if __name__ == '__main__':
    unittest.main()