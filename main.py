## T I C   T A C T I C S  v1.0 (Classic version)
## Created by Darius Brown

from random import randint
import time

## I. Board
def setBoard(b):
    for i in range(9): b[i] = str(i+1)

def printBoard(b):
    print('\n')
    print('       |       |       ')
    print('   '+b[0]+'   |   '+b[1]+'   |   '+b[2]+'   ')
    print('_______|_______|_______')
    print('       |       |       ')
    print('   '+b[3]+'   |   '+b[4]+'   |   '+b[5]+'   ')
    print('_______|_______|_______')
    print('       |       |       ')
    print('   '+b[6]+'   |   '+b[7]+'   |   '+b[8]+'   ')
    print('       |       |       ')
    print('\n')


## II. Input
def square(b,p):
    if(p == 1): p_letter = 'X'
    if(p == 2): p_letter = 'O'
    ch = input('Choose one of the numbers to place '+p_letter+':   ')
    while((len(ch) != 1) or (ord(ch) < 49 or ord(ch) > 57) or (b[int(ch)-1] == 'X' or b[int(ch)-1] == 'O') or (ch == 'quit')):
        try:
            if(ch == 'quit'): return 'break'
            if(b[int(ch)-1] == 'X' or b[int(ch)-1] == 'O'):
                ch = input('Space taken. Try again:   ')
        except IndexError: ch = input('Out of range. Try again:   ')
        except ValueError: ch = input('Input invalid. Try again:   ')
    for i in range(9):
        if(ch == b[i]): b[i] = p_letter


## III. Check Wins
def checkWin(b):
    win_letter = 'Z'

    if  (b[0] == b[1] == b[2]): win_letter = b[0]
    elif(b[3] == b[4] == b[5]): win_letter = b[3]
    elif(b[6] == b[7] == b[8]): win_letter = b[6]
    elif(b[0] == b[3] == b[6]): win_letter = b[0]
    elif(b[1] == b[4] == b[7]): win_letter = b[1]
    elif(b[2] == b[5] == b[8]): win_letter = b[2]
    elif(b[0] == b[4] == b[8]): win_letter = b[0]
    elif(b[2] == b[4] == b[6]): win_letter = b[2]

    if   win_letter == 'X': return 1
    elif win_letter == 'O': return 2

    for i in range(9):
        if(b[i] != 'X' and b[i] != 'O'): return 0
    return 3

def winStatus(b):
    if(checkWin(b) == 0): print('Game over - User Termination  \n')
    if(checkWin(b) == 1): print('Game over - X wins            \n')
    if(checkWin(b) == 2): print('Game over - O wins            \n')
    if(checkWin(b) == 3): print('Game over - Cat wins          \n')


## IV. Gameplay Mechanics
def menu(b):
    print('\n1. Play against human')
    print('2. Play against bot')
    ch = input('\nChoose game type:   ')
    gameplay(b,int(ch)-1)

def xomenu():
    print()
    print('1. Play as X')
    print('2. Play as O')
    ch = input('\nChoose player:   ')
    return int(ch)

def gameplay(b,g):
    ch = 'Y'
    if(g != 0): xo = xomenu()
    while(ch == 'Y' or ch == 'y'):      # loop for multiple games
        setBoard(b)
        for i in range(9):
            p = (i%2)+1
            printBoard(b)
            if(g == 0):
                if(square(b,p) == 'break'): break
            elif(g != 0):
                if(p == xo):
                    if(square(b,p) == 'break'): break
                else: bot(b,p,g)        # function for bot selection
            if(checkWin(b)!=0):
                printBoard(b)
                break
        winStatus(b)
        ch = input('Play again? Y/N: ')

def title_screen():
	print(
		"             Darius Brown Presents:\n"
		" _____ _        _____           _   _          \n"
		"/__   (_) ___  /__   \__ _  ___| |_(_) ___ ___ \n"
		"  / /\/ |/ __|   / /\/ _` |/ __| __| |/ __/ __|\n"
		" / /  | | (__   / / | (_| | (__| |_| | (__\__ \ \n"
		" \/   |_|\___|  \/   \__,_|\___|\__|_|\___|___/\n"
	)

def bot(b,p,g):
    if(g == 1): bot3(b,p)

## XX. Run the program
def run():
    title_screen()
    b = [''] * 9                        # creates tic tac toe board
    ch = 'Y'
    while(ch == 'Y' or ch == 'y'):      # loop for multiple matches
        menu(b)
        ch = input('New Game? Y/N:   ')
    print('Ending Program...')


## V. Artificial Intelligence (Bots)
# --------------------------------------------------------------------
## Tic Tactics Bot v3.0
## Created by Darius Brown

# features:
# - random selection process
# - defensive immediate response
# - win immediate response (if it sees a win on its turn)

def bot3(b,p):
    if(p == 1): 
        p_letter = 'X'
        op_letter = 'O'
    elif(p == 2):
        p_letter = 'O'
        op_letter = 'X'

    # Read in the board     ------------------------------------------
    d = [[]]*9                          # creates test board
    for i in range(9):                  # copies real board to test one
        d[i] = b[i]

    # Assessing situation   ------------------------------------------
    danger = 10                         # danger of losing - 10 value b/c of 9 available spaces
    chance = 10                         # opportunity of winning
    time.sleep(1)						# pause for realism

    for i in range(9):                  # checks for possible wins
        if(d[i] != 'X' and d[i] != 'O'):
            d[i] = p_letter
            if(checkWin(d) == (p)):
                chance = i
            d[i] = str(i+1)
    if(chance == 10):                   # if no possible wins found
        for i in range(9):              # checks for possible losses
            if(d[i] != 'X' and d[i] != 'O'):
                d[i] = op_letter        # try the next move for opponent letter
                if(checkWin(d) == ((p%2)+1)):
                    if(danger != 10):
                        print('Bot detected fork! At '+str(danger+1)+' & '+str(i+1)+'.')
                        break
                    else:
                        danger = i
                d[i] = str(i+1)         # set the board back to repeat again

    # Make the move         ------------------------------------------
    play = False
    if(chance != 10):                   # if it needs to take a win
        sp = chance
    elif(danger != 10):                 # if it needs to block a move
        sp = danger
    else:                               # or else it'll just pick randomly
        while(play != True):
            sp = randint(0, 8)
            if(b[sp] != 'X' and b[sp] != 'O'):
                play = True
    print('Bot chooses '+str(sp+1))
    b[sp] = p_letter

# --------------------------------------------------------------------

if __name__ == '__main__':
    run()