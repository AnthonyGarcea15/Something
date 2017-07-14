#Python Battleship
board = []

for x in range (5):
        board.append (["0"]*5)

def print_board (board):
        for row in board:
                print (*row, sep= ' ')
print_board (board)

from random import randint

def random_row(board):
        return (randint(0, len (board)-1))
def random_col(board) :
        return (randint(0, len(board[0])-1))

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range (5):
        print (turn+1)
        guess_row = int (input ("Guess Row"))
        guess_col = int (input ("Guess Column"))

        if guess_row == ship_row and guess_col == ship_col:
                print ("Congratulations, You Won")
                break 
        else:
                if (guess_row < 0 or guess_row >4) or (guess_col < 0 or guess_col >4):
                        print ("Please enter coordinate within the Board")
                elif (board[guess_row][guess_col] == "x"):
                        print ("You've already guessed that!")
                else:
                        print ("Sorry, Guess again")
                        board[guess_row][guess_col] = "x"
                        print_board(board)
                if turn == 4:
                        print ("Game Over!")
                        


        
        



