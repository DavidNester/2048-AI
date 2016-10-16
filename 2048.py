from twenty48 import Board_2048
from expectimax2048 import ExpectimaxAgent
import curses
import copy


def main():
    board = Board_2048()
    agent = ExpectimaxAgent()
    game = True
    score = 0
    old_board = board
    while game:
        
        #board.print_board()
        row1,row2,row3 = board.board_string()
        #print score
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(1)
        stdscr.addstr(10,30,row1)
        stdscr.addstr(12,30,row2)
        stdscr.addstr(14,30,row3)
        stdscr.addstr(16,30,"Score: " + str(score))
        stdscr.addstr(18,30,agent.getAction(board))
        key = stdscr.getch()
        #register key press up down left right
        if key == curses.KEY_UP:
            new_board,moves,new_score = board.up()
        elif key == curses.KEY_LEFT:
            new_board,moves,new_score = board.left()
        elif key == curses.KEY_DOWN:
            new_board,moves,new_score = board.down()
        elif key == curses.KEY_RIGHT:
            new_board,moves,new_score = board.right()
        else:
            new_board = board
            new_score = 0
        board = new_board
        score += new_score
        
        
        if board.check_end():
            game = False
    curses.endwin()
    
    
    board.print_board()
    print "Final Score: " + str(score)
    
if __name__ == "__main__":
    main()