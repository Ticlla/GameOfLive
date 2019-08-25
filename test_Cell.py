import unittest
from cell import Cell


class CellTest(unittest.TestCase):
	
	def test_cell_class(self):
		cellTest = Cell(False)
		self.assertIsInstance(cellTest, Cell, "Class Should be Cell")

	def test_ALIVE_state(self):
		input_state = Cell.ALIVE
		expected_state = 1
		self.assertEqual(expected_state,input_state)

	def test_DEATH_state (self):
		input_state = Cell.DEATH
		expected_state = 0
		self.assertEqual(expected_state,input_state)		











if __name__ == '__main__':
    unittest.main()