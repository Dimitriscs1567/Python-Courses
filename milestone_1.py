from random import randint

playing = True
O_LETTER = "O"
X_LETTER = "X"
DRAW = "draw"
EMPTY_BOARD = " "

def selectEachPlayerLetter():
    player_1 = input("Give first player letter: ")
    while player_1.capitalize() != X_LETTER and player_1.capitalize() != O_LETTER:
        player_1 = input(f"Please select {O_LETTER} or {X_LETTER}: ")
    player_1 = player_1.capitalize()

    player_2 = X_LETTER if player_1 == O_LETTER else O_LETTER

    return (player_1, player_2)

def getHit(turn, board):
    stringHit = input(f"Give player {turn} choice (1-9): ")
    hit = int(stringHit)
    accepted = False if hit > 9 or hit < 1 or board[hit - 1] != EMPTY_BOARD else True

    while not accepted:
        if hit > 9 or hit < 1:
            stringHit = input(f"Please choose 1-9 for player {turn} choice: ")
        else:
            stringHit = input(f"Please an empty block for player {turn} choice: ")
           
        hit = int(stringHit)
        accepted = False if hit > 9 or hit < 1 or board[hit - 1] != EMPTY_BOARD else True

    return hit

def checkWin(board):
    winCases = [None, None, None, None, None, None, None, None]

    winCases[0] = board[0] if board[0] == board[1] and board[1] == board[2] and board[0] != EMPTY_BOARD else None
    winCases[1] = board[3] if board[3] == board[4] and board[4] == board[5] and board[3] != EMPTY_BOARD else None
    winCases[2] = board[6] if board[6] == board[7] and board[7] == board[8] and board[6] != EMPTY_BOARD else None
    winCases[3] = board[0] if board[0] == board[3] and board[3] == board[6] and board[0] != EMPTY_BOARD else None
    winCases[4] = board[1] if board[1] == board[4] and board[4] == board[7] and board[1] != EMPTY_BOARD else None
    winCases[5] = board[2] if board[2] == board[5] and board[5] == board[8] and board[2] != EMPTY_BOARD else None
    winCases[6] = board[0] if board[0] == board[4] and board[4] == board[8] and board[0] != EMPTY_BOARD else None
    winCases[7] = board[2] if board[2] == board[4] and board[4] == board[6] and board[2] != EMPTY_BOARD else None

    win = list(filter(lambda value: value != None, winCases))
    if(len(win) > 0):
        return win[0]  

    win = list(filter(lambda value: value == EMPTY_BOARD, board))
    if(len(win) == 0):
        return DRAW
    
    return None

def printBoard(board):
    for i in range(len(board)):
        if i%3 == 0:
            print("\n| ", end = "")
        print(f"{board[i]} | ", end = "")

    print("\n\n")

while playing:
    (player_1, player_2) = selectEachPlayerLetter()
    board = [EMPTY_BOARD, EMPTY_BOARD, EMPTY_BOARD, EMPTY_BOARD, EMPTY_BOARD, EMPTY_BOARD, EMPTY_BOARD, EMPTY_BOARD, EMPTY_BOARD]
    win = None
    turn = randint(1,2)

    while win == None:
        hit = getHit(turn, board)
        board[hit - 1] = player_1 if turn == 1 else player_2
        printBoard(board)
        win = checkWin(board)
        turn = 1 if turn == 2 else 2

    if win == player_1:
        print("Player 1 wins!!!")
    elif win == player_2:
        print("Player 2 wins!!!")
    else:
        print("It is a draw!!!")

    playAgain = input("Do you want to play again?(y-n) ")
    while playAgain.lower() != "y" and playAgain.lower() != "n":
        playAgain = input("Please choose a valid option (y-n): ")

    if playAgain.lower() == "n": playing = False
