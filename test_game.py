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


if __name__ == '__main__':
    unittest.main()