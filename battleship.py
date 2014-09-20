Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from random import randint

# create empty board
board = []

# adding locations
for x in range(5):
    board.append(["O"] * 5)

# print board
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

#generates a random location
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# assign random location to a ship row & col
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Guessing Game! The fun part! :)
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break 
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col         > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
    print "Turn", turn + 1
    print_board(board)