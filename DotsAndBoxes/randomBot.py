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

while True:
	move = generateRandomMove(state)
	state.move(move[:2],move[2])
	sys.stdout.write(move + '\n')
	sys.stdout.flush()
	moves = raw_input().split(' ')
	for move in moves:
		state.move(move[:2],move[2])
