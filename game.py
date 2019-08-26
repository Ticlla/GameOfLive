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

	# getCell  retrieves cell at specific location on matrix
	# row, col : row number and column number
	def getCell(self,row, col):
		return self.board[row][col]

	# Gets The number of neigbors a cell can have, it considers all possible scenarios
	def getNumberNeighbours(self, row, col):
		right_neighbour = Cell.DEATH if (col + 1 >= len(self.board[0])) else self.board[row][col + 1].state
		left_neighbour = Cell.DEATH if (col - 1 < 0) else self.board[row][col - 1].state
		top_neighbour = Cell.DEATH if (row - 1 < 0) else self.board[row - 1][col].state
		bottom_neighbour = Cell.DEATH if (row + 1 >= len(self.board)) else self.board[row + 1][col].state
		top_corner_left_neighbour = Cell.DEATH if (row - 1 < 0 or col - 1 < 0) else self.board[row - 1][col - 1].state
		top_corner_right_neighbour = Cell.DEATH if (row - 1 < 0 or col + 1 >= len(self.board[0])) else self.board[row - 1][col + 1].state
		bottom_corner_left_neighbour = Cell.DEATH if (row + 1 >= len(self.board) or col - 1 < 0) else  self.board[row + 1][col - 1].state
		bottom_corner_right_neighbour = Cell.DEATH if (row + 1 >= len(self.board) or col + 1 >= len(self.board[0])) else self.board[row + 1][col + 1].state

		return right_neighbour + left_neighbour + top_neighbour + bottom_neighbour + top_corner_left_neighbour + top_corner_right_neighbour + bottom_corner_left_neighbour + bottom_corner_right_neighbour


	# nextGameState: it set the next board state 
	def nextGameState(self):
		aux_board = [[0 for i in range(len(self.board[0]))] for i in range(len(self.board))]
	
		for i in  range(len(self.board)):
			for j in   range(len(self.board[0])):
		 		number_neighbour = self.getNumberNeighbours(i,j)
		 		cell = self.getCell(i,j)
		 		aux_board[i][j] =  Cell(cell.get_next_state(number_neighbour))

		self.board = aux_board
		return self.board
