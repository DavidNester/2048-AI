from twenty48 import Board_2048
import random

class ExpectimaxAgent(object):
    
    def __init__(self, depth = '2'):
        self.weights = {}
        self.weights['score'] = .5
        self.weights['spaces'] = 35
        self.weights['pair'] = 25
        self.weights['difference'] = 4
        self.depth = int(depth)
        self.alpha = 0.8
        
    def getAction(self, board):
        legalMoves = board.poss_moves()
        scores = [self.recExpectimax(self.depth,1,board.generateSuccessor(action)) for action in legalMoves]
        #print legalMoves
        #print scores
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)
        return legalMoves[chosenIndex]
    
    def recExpectimax(self, depth, agent, board):
        if depth == 0 or board.check_end():
            return self.evaluate(board)
        if agent == 0:
            legalMoves= board.poss_moves()
            successors = [self.recExpectimax(depth,1, board.generateSuccessor(a)) for a in legalMoves]
            return max(successors)
        else:
            next_states = board.random_successors()
            probabilities = []
            for board,prob in next_states:
                successors = [self.recExpectimax(depth-1,0,board)]
                probabilities.append(prob)
            total = 0.0
            #print probabilities
            for i in range(len(successors)):
                total += probabilities[i]*successors[i]
            return total
    
    def update(self,board,action,nextBoard,reward):
        best = float("-inf")
        for a in self.possMoves(nextBoard):
            new = self.evaluate(nextBoard,a)#figure out what this should be
            if new>best:
                best = new
        if best == float("-inf"):
            best = 0

        features = board.get_features()
        difference = (reward + best) - self.evaluate(board,action)#figure out what this should be
        for feature in features:#may need changes here
            self.weights[feature] = self.weights[feature] + self.alpha*difference*features[feature]

    def evaluate(self, board):
        features = board.get_features()
        return self.weights['score']*features['s'] + self.weights['spaces']*features['space'] + self.weights['pair']*features['pair'] - self.weights['difference']*features['difference']
        #Advice from:
        #http://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048


corners = [(0,0),(2,0),(0,2),(2,2)]