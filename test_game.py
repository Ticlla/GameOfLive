import unittest
from game import Game
from cell import Cell


class GameTest(unittest.TestCase):

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





if __name__ == '__main__':
    unittest.main()