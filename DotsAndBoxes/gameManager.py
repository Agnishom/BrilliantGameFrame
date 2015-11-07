from gameStruct import gameState
import subprocess
import threading

#for timing mechanism
def timeexceeded(player):
	print ("Player " + player + " exceeded the time limit")
	logFile.write("Player " + player + " exceeded the time limit\n")

#Create connection to bot 1
botA = subprocess.Popen(raw_input("Enter command to Bot A: ").split(" "),stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#Create connection to bot 2
botB = subprocess.Popen(raw_input("Enter command to Bot B: ").split(" "),stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#Create log file
logFile = open(raw_input("Enter log file name: "),"w")

#Create a new game instance
state = gameState()

#Tell the bots that they are players A and B respectively.
botA.stdin.write('A\n')
logFile.write('A\n')
botA.stdin.flush()
botB.stdin.write('B\n')
logFile.write('B\n')
botB.stdin.flush()

#Game Loop
new_player = state.player
moves = []

while not state.isGameOver():

	#Accept a new move in 5 seconds
	timer = threading.Timer(5.0, lambda: timeexceeded(new_player))
	timer.start()
	new_move = {'A': botA, 'B': botB}[new_player].stdout.readline()[:-1]
	timer.cancel()

	#validate move
	try:
		state.move(new_move[:2],new_move[2])
	except:
		print "Error with bot " + new_player
		break

	moves.append(new_move)

	#If the player has changed tell the new player what the previous player did
	if state.player != new_player:
		new_player = state.player
		{'A': botA, 'B': botB}[new_player].stdin.write(" ".join(moves) + "\n")
		#The following line is fine
		logFile.write({'A': "Player B: ", 'B': "Player A: "}[new_player])
		logFile.write(" ".join(moves) + "\n")
		{'A': botA, 'B': botB}[new_player].stdin.flush()
		logFile.flush()
		moves = []

botA.stdin.write('halt\n')
logFile.write("halt\n")
botA.stdin.flush()
botB.stdin.write('halt\n')
logFile.write("halt\n")
botB.stdin.flush()

logFile.write("Score A: " + str(state.score['A']) + '\n')
logFile.write("Score B: " + str(state.score['B']) + '\n')

logFile.close()

#Show the game state just for visual pleasure
#print state
