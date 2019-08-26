from game import Game
from cell import Cell
import time



initial_game_state = [
		[Cell.DEATH,Cell.ALIVE,Cell.DEATH],
		[Cell.DEATH,Cell.ALIVE,Cell.DEATH],
		[Cell.DEATH,Cell.ALIVE,Cell.DEATH]
		]

game = Game(initial_game_state)

for i in range(1000):
	print (game)
	game.nextGameState()
	time.sleep(1)
