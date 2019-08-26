from cell import Cell

class Game:
	
	def __init__(self, board):
		self.board = [[0 for i in range(len(board[0]))] for i in range(len(board))]
	
		for i in  range(len(board)):
			for j in   range(len(board[0])):
		 		self.board[i][j] =  Cell(board[i][j])
		

	

	def __str__(self):
		board_text = ""
		for i in  range(len(self.board)):
				for j in   range(len(self.board[0])):
					board_text = board_text + str(self.board[i][j])
				board_text = board_text + "\n"


		return board_text

#board = [
#		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
#		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
#		[Cell.ALIVE,Cell.DEATH,Cell.ALIVE],
#		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
#		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE],
#		[Cell.ALIVE,Cell.ALIVE,Cell.ALIVE]
#		]

#print (Game(board))
#print("a" + "b")