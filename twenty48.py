import random
import copy
import math

class Board_2048(object):

    def __init__(self, rows=None):
        if not rows:
            rows = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
            self.rows = list(rows)
            self.add_2()
            self.add_2()
        else:
            self.rows = list(rows)

    #returns new board, moves(used for pygame version), and score change
    def _moveh(self, loop_list, jstep):
        score = 0
        moves = set()
        new_board = copy.deepcopy(self)
        for i in loop_list:
            combined = False#changed if moved to 4x4
            for j in loop_list:
                index = j + jstep
                real = j
                zeros = True
                moved = False
                change = 0
                if new_board.rows[i][j] != 0:
                    while zeros:
                        if index > -1 and index < 3:
                            if new_board.rows[i][index] == 0:
                                new_board.rows[i][index] = new_board.rows[i][j]
                                new_board.rows[i][j] = 0
                                index += jstep
                                j += jstep
                                change = -jstep
                                moved = True
                            elif new_board.rows[i][index] == new_board.rows[i][j]:
                                if not combined:#changed if 4x4
                                    new_board.rows[i][index] = new_board.rows[i][index]*2
                                    new_board.rows[i][j] = 0
                                    moved = True
                                    combined = True#changed if 4x4
                                    change = 0
                                    score += new_board.rows[i][index] 
                                else:
                                    zeros = False
                            else:
                                zeros = False
                        else:
                            zeros = False
                if moved:
                    moves.add((i, real, i, index+change))
        if moves == set():
            return self, set(),0
        else:
            return new_board, moves, score

    def left(self):
        loop_list = range(0,3)
        jstep = -1
        board, moves, s = self._moveh(loop_list, jstep)
	if len(moves) > 0:
	    board.add_2()
	return board, moves, s

    def right(self):#needs to be changed
        loop_list = backwards
        jstep = 1
        board, moves, s =  self._moveh(loop_list, jstep)
	if len(moves) > 0:
	    board.add_2()
	return board, moves, s
    
    #returns new board, moves(used for pygame version), and score change
    def _movev(self, loop_list, istep):
        score = 0
        moves = set()
        new_board = copy.deepcopy(self)
        for j in loop_list:
            combined = False
            for i in loop_list:
                index = i + istep 
                real = i
                zeros = True
                moved = False
                change = 0
                if new_board.rows[i][j] != 0:
                    while zeros:
                        if index > -1 and index < 3:
                            if new_board.rows[index][j] == 0:
                                new_board.rows[index][j] = new_board.rows[i][j]
                                new_board.rows[i][j] = 0
                                index += istep
                                i += istep
                                change = -istep
                                moved = True
                            elif new_board.rows[index][j] == new_board.rows[i][j]:
                                if not combined:
                                    new_board.rows[index][j] = new_board.rows[index][j]*2
                                    new_board.rows[i][j] = 0
                                    moved = True
                                    combined = True#changed if 4x4
                                    change = 0
                                    score += new_board.rows[index][j]
                                else:
                                    zeros = False
                            else:
                                zeros = False
                        else:
                            zeros = False
                if moved:
                    moves.add((real, j, index + change, j))
        if moves == set():
            return self, set(),0
        else:
            return new_board, moves, score
    
    def up(self):
        loop_list = range(0,3)
        istep = -1
        board, moves, s = self._movev(loop_list, istep)
	if len(moves) > 0:
	    board.add_2()
	return board, moves, s
        
    def down(self):#needs to be changed
        loop_list = backwards
        istep = 1
        board, moves, s =  self._movev(loop_list, istep)
	if len(moves) > 0:
	    board.add_2()
	return board, moves, s
    
    def print_board(self):
	row1,row2,row3 = self.board_string()
	print row1
	print row2
	print row3
    
    def board_string(self):
	row1 = ''
	row2 = ''
	row3 = ''
	for i in range(3):
	    row1 += str(self.rows[0][i])
	    if self.rows[0][i]/10 == 0:
		row1 += '   '
	    elif self.rows[0][i]/10 < 10:
		row1 += '  '
	    elif self.rows[0][i]/10 < 100:
		row1 += ' '
	for i in range(3):
	    row2 += str(self.rows[1][i])
	    if self.rows[1][i]/10 == 0:
		row2 += '   '
	    elif self.rows[1][i]/10 < 10:
		row2 += '  '
	    elif self.rows[1][i]/10 <100:
		row2 += ' '
	for i in range(3):
	    row3 += str(self.rows[2][i])
	    if self.rows[2][i]/10 == 0:
		row3 += '   '
	    elif self.rows[2][i]/10 < 10:
		row3 += '  '
	    elif self.rows[2][i]/10 < 100: 
		row3 += ' '
	return row1,row2,row3
    
    #randomly adds a 2 or 4 to one of the open spaces
    def add_2(self):
        open_spaces = self.open_spaces()
        number = random.randint(0,len(open_spaces)-1)
        i,j = open_spaces[number]
        new_value = 0
        r = random.random()
        if r - .9 > 0:
            new_value = 4
        else:
            new_value = 2
        self.rows[i][j] = new_value
    
    #checks for end of game
    def check_end(self):
	for i in range(3):
	    for j in range(3):
		if self.rows[i][j] == 0:
		    return False
	for row in self.rows:
	    if self._check(row):
		return False
	for i in range(3):
	    row = []
	    for j in range(3):
	       row.append(self.rows[j][i])
	    if self._check(row):
		return False
	return True
    
    #checks row for a pair next to each other
    def _check(self, row):
	same = False
	if row[0] == row[1]:
	    same = True
	if row[1] == row[2]:
	    same = True
	return same
    
    #returns list of open spaces on board
    def open_spaces(self):
        open_space = list()
        for i in range(0,3):
            for j in range(0,3):
                if self.rows[i][j] == 0:
                    open_space.append((i,j))
        return open_space
    
    #returns number of adjacent pairs
    def pairs(self):
	total = 0
	for j in range(3):
	    for i in range(2):
		if self.rows[i][j] == self.rows[i+1][j]:
		    total += 1
	for i in range(3):
	    for j in range(2):
		if self.rows[i][j] == self.rows[i][j+1]:
		    total += 1
	return total
    
    
    #returns list of possible moves
    def poss_moves(self):
	moves = []
	boardu, motionsu, scoreu = self._movev(range(0,3),-1)
	boardr, motionsr, scorer = self._moveh(backwards,1)
        boardl, motionsl, scorel = self._moveh(range(0,3),-1)
        boardd, motionsd, scored = self._movev(backwards,1)
	if len(motionsr) != 0:
	    moves.append('right')
        if len(motionsu) != 0:
	    moves.append('up')
	if len(motionsl) != 0:
	    moves.append('left')
        if len(motionsd) !=0:
	    moves.append('down')
        return moves
    
    #returns list of successors for when a random space is filled along with the probability
    def random_successors(self):
	successors = []
	spaces = self.open_spaces()
	for space in spaces:
	    i,j = space
	    new = copy.deepcopy(self)
	    new.rows[i][j] = 2
 	    successors.append((new,1.0/float(len(spaces))*.9))
	    new.rows[i][j] = 4
	    successors.append((new,1.0/float(len(spaces))*.9))
	return successors
    
    #returns successor board after action is made without the add_2 part
    def generateSuccessor(self, action):
	new_board = copy.deepcopy(self)
	if action == 'left':
	    board,m,s = new_board._moveh(range(0,3),-1)
	elif action == 'right':
	    board,m,s = new_board._moveh(backwards,1)
	elif action == 'up':
	    board,m,s = new_board._movev(range(0,3),-1)
	elif action == 'down':
	    board,m,s = new_board._movev(backwards,1)
	return board
    
    #returns sum of differences between all adjacent squares
    def adjacent_differences(self):
	total = 0
	for j in range(3):
	    for i in range(2):
		if self.rows[i][j] != 0 and self.rows[i+1][j] != 0:
		    total += abs(self.rows[i][j] - self.rows[i+1][j])
	for i in range(3):
	    for j in range(2):
		if self.rows[i][j] != 0 and self.rows[i][j+1] != 0:
		    total += abs(self.rows[i][j] - self.rows[i][j+1])
	return total
    def score(self):
	score = 0.0
        for i in range(3):
            for j in range(3):
                if self.rows[i][j] != 0:
                    score += (math.log(self.rows[i][j],2)-1)*self.rows[i][j]
	return score
    def get_features(self):
	features = {}
	features['difference'] = self.adjacent_differences()
	features['pair'] = self.pairs()
	features['space'] = len(self.open_spaces())
	features['s'] = self.score()
	return features

backwards = (2,1,0)

