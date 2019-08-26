class Cell():
	ALIVE = 1
	DEATH = 0

	def __init__(Self, state):
		Self.state = state


	def get_next_state(Self,neighbours):
		if (Self.state == Cell.ALIVE):
			if (neighbours == 2 or neighbours == 3):
				return Cell.ALIVE
		elif (Self.state == Cell.DEATH ):
			if (neighbours == 3):
				return Cell.ALIVE
		return Self.DEATH


	def __str__(self):
		if self.state == 1:
			return 'o'
		else:
			 return '.'