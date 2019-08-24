import unittest

class MathTest(unittest.TestCase):
	
	def test_assert(self):
		initial_value = 2
		expected_value = 4
		self.assertEqual(initial_value,expected_value,f'Asserting {initial_value}:{expected_value}')


if __name__ == '__main__':
    unittest.main()