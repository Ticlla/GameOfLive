import unittest
from cell import Cell


class CellTest(unittest.TestCase):
	
	def test_cell_class(self):
		cellTest = Cell(Cell.ALIVE)
		self.assertIsInstance(cellTest, Cell, "Class Should be Cell")

	def test_alive_state(self):
		input_state = Cell.ALIVE
		expected_state = 1
		self.assertEqual(expected_state,input_state)

	def test_death_state (self):
		input_state = Cell.DEATH
		expected_state = 0
		self.assertEqual(expected_state,input_state)		

	def test_cell_alive(self):
		cellTest = Cell(Cell.ALIVE)
		input_state = cellTest.state
		expected_state = Cell.ALIVE
		self.assertEqual(input_state, expected_state)

	def test_cell_death(self):
		cellTest = Cell(Cell.DEATH)
		input_state = cellTest.state
		expected_state = Cell.DEATH
		self.assertEqual(input_state, expected_state)










if __name__ == '__main__':
    unittest.main()