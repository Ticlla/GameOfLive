import unittest
from cell import Cell


class CellTest(unittest.TestCase):
	
	# Test Cell calss to have Specifi Class name
	def test_cell_class(self):
		cellTest = Cell(Cell.ALIVE)
		self.assertIsInstance(cellTest, Cell, "Class Should be Cell")

	# Test Alive state	
	def test_alive_state(self):
		input_state = Cell.ALIVE
		expected_state = 1
		self.assertEqual(expected_state,input_state)

	# Test Death state
	def test_death_state (self):
		input_state = Cell.DEATH
		expected_state = 0
		self.assertEqual(expected_state,input_state)		

	# Test a CEll Alive state
	def test_cell_alive(self):
		cellTest = Cell(Cell.ALIVE)
		input_state = cellTest.state
		expected_state = Cell.ALIVE
		self.assertEqual(expected_state,input_state)		

	# Test death cell state
	def test_cell_death(self):
		cellTest = Cell(Cell.DEATH)
		input_state = cellTest.state
		expected_state = Cell.DEATH
		self.assertEqual(expected_state,input_state)		

	# Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
	def test_cell_overpopulation(self):
		cellTest = Cell(Cell.ALIVE)
		neighbors_live = 4
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.DEATH
		self.assertEqual(expected_state, next_state)

		neighbors_live = 5
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.DEATH
		self.assertEqual(expected_state, next_state)


	#Stasis: if a living cell is surrounded by two or three living cells, it survives.
	def test_cell_stasis(self):
		cellTest = Cell(Cell.ALIVE)
		neighbors_live = 2
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.ALIVE
		self.assertEqual(expected_state, next_state)

		neighbors_live = 3
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.ALIVE
		self.assertEqual(expected_state, next_state)

	#Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
	def test_cell_underpopulation(self):
		cellTest = Cell(Cell.ALIVE)
		neighbors_live = 0
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.DEATH
		self.assertEqual(expected_state, next_state)

		neighbors_live = 1
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.DEATH


	#Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.
	def test_cell_reproduction(self):
		cellTest = Cell(Cell.DEATH)
		neighbors_live = 3
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.ALIVE
		self.assertEqual(expected_state, next_state)

		cellTest = Cell(Cell.DEATH)
		neighbors_live = 2
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.DEATH
		self.assertEqual(expected_state, next_state)

		cellTest = Cell(Cell.DEATH)
		neighbors_live = 4
		next_state = cellTest.get_next_state(neighbors_live)
		expected_state = Cell.DEATH
		self.assertEqual(expected_state, next_state)





if __name__ == '__main__':
    unittest.main()