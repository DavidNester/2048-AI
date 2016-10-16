from twenty48 import Board_2048
from expectimax2048 import ExpectimaxAgent

def main():
    board = Board_2048()
    agent = ExpectimaxAgent()
    game = True
    score = 0
    print "Game with Expectimax depth 2 with moves shown:"
    #board.print_board()
    #print score
    while game:
        move = agent.getAction(board)
        if move == 'right':
            new_board,moves,s = board.right()
        elif move == 'left':
            new_board,moves,s = board.left()
        elif move == 'up':
            new_board,moves,s = board.up()
        elif move == 'down':
            new_board,moves,s = board.down()
        board = new_board
        score += s
        #print move
        #board.print_board()
        #print score
        
        if board.check_end():
            game = False
    print
    board.print_board()
    print "Final Score: " + str(score)
    print
    print
    analysis()

def analysis():
    total = 0
    maxScore = 0
    for i in range(100):
        board = Board_2048()
        agent = ExpectimaxAgent(1)
        game = True
        score = 0
        while game:
            move = agent.getAction(board)
            if move == 'right':
                new_board,moves,s = board.right()
            elif move == 'left':
                new_board,moves,s = board.left()
            elif move == 'up':
                new_board,moves,s = board.up()
            elif move == 'down':
                new_board,moves,s = board.down()
            board = new_board
            score += s    
            if board.check_end():
                game = False
        #board.print_board()
        #print "Final Score: " + str(score)
        total += score
        if score > maxScore:
            maxScore = score
    print "Average Score After 100 Games Depth 1: " + str(float(total/100))
    print "Max(Depth 1): " + str(maxScore)
    maxScore=0
    total = 0
    for i in range(100):
        board = Board_2048()
        agent = ExpectimaxAgent()
        game = True
        score = 0
        while game:
            move = agent.getAction(board)
            if move == 'right':
                new_board,moves,s = board.right()
            elif move == 'left':
                new_board,moves,s = board.left()
            elif move == 'up':
                new_board,moves,s = board.up()
            elif move == 'down':
                new_board,moves,s = board.down()
            board = new_board
            score += s    
            if board.check_end():
                game = False
        #board.print_board()
        #print "Final Score: " + str(score)
        total += score
        if score > maxScore:
            maxScore = score
    print "Average Score After 100 Games Depth 2: " + str(float(total/100))
    print "Max(Depth 2): " + str(maxScore)
    
    
if __name__ == "__main__":
    main()