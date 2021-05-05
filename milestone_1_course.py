from random import randint

def winCondition(board):
    if board[0] == board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] == board[8]: 
        return board[6]
    elif board[0] == board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]
    elif board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]

    if len(list(filter(lambda el: el == "", board))) == 0:
        return "Draw"

    return ""

def isEmpty(el):
    return el == ""
    

def boardPrint(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print()

        if board[i] == "":
            print(" ", end = " | ")
        else:
            print(board[i], end = " | ")

    print()

keepPlaying = True

while keepPlaying: 
    player1 = ""
    player2 = ""
    board = ["", "", "", "", "", "", "", "", ""]

    player1 = input("Give first player letter (O, X): ")
    while player1.capitalize() != "X" and player1.capitalize() != "O":
        player1 = input("Please give an O or an X: ")

    player1 = player1.capitalize()
    if player1 == "O":
        player2 = "X"
    else:
        player2 = "O"

    #player2 = "X" if player1 == "O" else "O"

    first = randint(1, 2)

    print(f"The first player is player {first}")

    playing = True

    while playing:
        hit = input(f"Give player 's {first} choice (1-9): ") #ALWAYS gives a string
        hit = int(hit) #Convert the string given by input to integer 
        while hit < 1 or hit > 9 or board[hit - 1] != "":
            hit = input(f"Give player 's {first} choice (1-9): ")
            hit = int(hit)
        
        board[hit - 1] = player1 if first == 1 else player2
        boardPrint(board)

        winningPlayer = winCondition(board)
        if winningPlayer != "":
            if winningPlayer == player1:
                print("Player 1 won.")
            elif winningPlayer == player2:
                print("Player 2 won.")
            else:
                print("It is a draw!")

            playing = False


        first = 1 if first == 2 else 2

    choice = input("Do you want to keep playing? (y-n): ")
    keepPlaying = choice == "y"
        