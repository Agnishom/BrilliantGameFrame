#Script for Dots and Boxes contest

class gameState:
	def __init__(self,m=8,n=8):
		'''setup an empty board of m rows and n columns'''
		self.m = m
		self.n = n
		#Top, Left, Bottom, Right, Player
		self.board = [ [ [False, False, False, False, None] for i in xrange(n) ] for j in xrange(m)]
		#Legal Player
		self.player = 'A'
		#scores
		self.score = {'A': 0,'B': 0}
	def __getitem__(self,pos):
		'''Accept a move in chess style notation like A1, B4, etc'''
		#Which Column?
		n = ord(pos[0]) - 65
		#Which Row?
		m = self.m - int(pos[1])
		return self.board[m][n]
	def __str__(self):
		'''Compact game notation'''
		s = ""
		for i in xrange(self.m):
			for j in xrange(self.n):
				#Top, Left, Bottom, Right, Player
				s += "^" if self.board[i][j][0] else "."
				s += "<" if self.board[i][j][1] else "."
				s += "v" if self.board[i][j][2] else "."
				s += ">" if self.board[i][j][3] else "."
				s += self.board[i][j][4] if self.board[i][j][4] else "."
				s += "" if j == self.n - 1 else " "
			s += "" if i == self.m - 1 else "\n"
		return s
	def valid(self, pos, move):
		'''Is <move> on <pos> a valid move?'''
		return self[pos][{'T': 0, 'L': 1, 'B': 2, 'R': 3}[move]] == False
	def neighbor(self,pos,direction):
		'''Find a neighbor in the given direction'''
		if direction == 'T':
			if int(pos[1]) == self.m:
				return None
			else:
				return pos[0] + str(int(pos[1])+1)
		elif direction == 'L':
			if pos[0] == 'A':
				return None
			else:
				return chr(ord(pos[0])-1) + pos[1]
		elif direction == 'B':
			if pos[1] == '1':
				return None
			else:
				return pos[0] + str(int(pos[1])-1)
		elif direction == 'R':
			if ord(pos[0]) == 65 + self.n - 1:
				return None
			else:
				return chr(ord(pos[0])+1) + pos[1]			
	def move(self, pos, move):
		'''Accept moves'''
		boxCompleted = False
		#Decode moves from TLBR
		seg = {'T': 0, 'L': 1, 'B': 2, 'R': 3}[move]
		#Has anyone taken this segment before?
		assert self.valid(pos, move)
		#Turn on the segment for this box
		self[pos][seg] = True
		#Check if a box is completed here
		if all(self[pos][:4]):
			self[pos][4] = self.player
			self.score[self.player] += 1
			boxCompleted = True
		#Select the neighbor
		neighbor = self.neighbor(pos,move)
		#Do the same things with the neighbor cell, if any
		complement = {'T': 'B', 'L': 'R', 'B': 'T', 'R': 'L'}[move]
		seg = {'T': 0, 'L': 1, 'B': 2, 'R': 3}[complement]
		if neighbor:
			self[neighbor][seg] = True
			if all(self[neighbor][:4]):
				self[neighbor][4] = self.player
				self.score[self.player] += 1
				boxCompleted = True
		#Another chance if a box is completed
		if not boxCompleted:
			self.player = 'B' if self.player == 'A' else 'A'
	def isGameOver(self):
		'''Check if game is over'''
		return self.score['A'] + self.score['B'] == self.m*self.n

def parse(string,player):
	'''Construct a class given the compact game notation and the current player'''
	string = map(lambda x: x.split(' '), string.split('\n'))
	m = len(string)
	n = len(string[0])
	state = gameState(m, n)
	for i in xrange(m):
		for j in xrange(n):
			if string[i][j][0] == '^': state.board[i][j][0] = True
			if string[i][j][1] == '<': state.board[i][j][1] = True
			if string[i][j][2] == 'v': state.board[i][j][2] = True
			if string[i][j][3] == '>': state.board[i][j][3] = True
			if string[i][j][4] != '.':
				state.board[i][j][4] = string[i][j][4]
				state.score[string[i][j][4]] += 1
	state.player = player
	return state