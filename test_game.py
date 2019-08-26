import unittest
from game import Game
from cell import Cell


class GameTest(unittest.TestCase):

	def test_initialize_game_state(self):
		initial_game_state = [
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE]
		]
		game = Game(initial_game_state)
		expected_game_state = [
		[Cell(Cell.ALIVE),Cell(Cell.ALIVE),Cell(Cell.ALIVE)],
		[Cell(Cell.ALIVE),Cell(Cell.ALIVE),Cell(Cell.ALIVE)],
		[Cell(Cell.ALIVE),Cell(Cell.ALIVE),Cell(Cell.ALIVE)]
		]

		for i in range(len(initial_game_state)):
			for j in range(len(initial_game_state[0])):
				if initial_game_state[i][j] == 1:
					expected = 'o'
				else: 
					expected = '.'

				self.assertEqual(str(game.board[i][j]), expected)
		#self.assertListEqual([1,2,3],[1,2,3,4])




if __name__ == '__main__':
    unittest.main()