import random
import sys
from gameStruct import gameState

def generateRandomMove(board):
	while True:
		pos = random.choice(['A','B','C','D','E','F','G','H']) + str(random.choice(range(1,9)))
		move = random.choice(['T','L','B','R'])
		if board.valid(pos,move):
			return pos+move

playOrder = raw_input()

state = gameState()

if playOrder == 'B':
	moves = raw_input().split(' ')
	for move in moves:
		state.move(move[:2],move[2])

switchPlayersFlag = False

while True:
	old_player = state.player
	move = generateRandomMove(state)
	state.move(move[:2],move[2])
	if state.player != old_player:
		switchPlayersFlag = True
	sys.stdout.write(move + '\n')
	sys.stdout.flush()
	if switchPlayersFlag:
		moves = raw_input()
		if 'halt' in moves:
			sys.exit()
		moves = moves.split(' ')
		for move in moves:
			state.move(move[:2],move[2])
		switchPlayersFlag = False
