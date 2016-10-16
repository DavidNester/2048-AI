from random import randint

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
    
    def move_left(self):
        for i in range(0,3):
            for j in range(0,3):
                index = j - 1
                if index > -1 and index < 3:
                    if self.rows[i][index] == 0:
                        self.rows[i][index] = self.rows[i][j]
                        self.rows[i][j] = 0
                    elif self.rows[i][index] == self.rows[i][j]:
                        self.rows[i][index] = self.rows[i][index]*2
                        self.rows[i][j] = 0
        self.add_2()
        print self.rows
    
    def move_right(self):#needs to be changed
        for i in backwards:
            for j in backwards:
                index = j + 1
                if index > -1 and index < 3:
                    if self.rows[i][index] == 0:
                        self.rows[i][index] = self.rows[i][j]
                        self.rows[i][j] = 0
                    elif self.rows[i][index] == self.rows[i][j]:
                        self.rows[i][index] = self.rows[i][index]*2
                        self.rows[i][j] = 0
                    
        self.add_2()
        print self.rows
    
    def move_up(self):
        for i in range(0,3):
            for j in range(0,3):
                index = i - 1
                if index > -1 and index < 3:
                    if self.rows[index][j] == 0:
                        self.rows[index][j] = self.rows[i][j]
                        self.rows[i][j] = 0
                    elif self.rows[index][j] == self.rows[i][j]:
                        self.rows[index][j] = self.rows[index][j]*2
                        self.rows[i][j] = 0
        self.add_2()
        print self.rows
    
    def move_down(self):#needs to be changed
        for i in backwards:
            for j in backwards:
                index = i + 1
                if index > -1 and index < 3:
                    if self.rows[index][j] == 0:
                        self.rows[index][j] = self.rows[i][j]
                        self.rows[i][j] = 0
                    elif self.rows[i][index] == self.rows[i][j]:
                        self.rows[index][j] = self.rows[index][j]*2
                        self.rows[i][j] = 0
        self.add_2()
        print self.rows
        
    def print_board(self):
        for i in range(0,3):
            print 'row %s' % i
            for j in range(0,3):
                print self.rows[i][j]
    
    def add_2(self):
        open_spaces = self.open_spaces()
        number = randint(0,len(open_spaces)-1)
        i,j = open_spaces[number]
        self.rows[i][j] = 2
    
    def open_spaces(self):
        open_space = list()
        for i in range(0,3):
            for j in range(0,3):
                if self.rows[i][j] == 0:
                    open_space.append((i,j))
        return open_space

backwards = (2,1,0)

