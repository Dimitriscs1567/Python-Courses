from random import randint

def winCondition(board):
    pass

def boardPrint(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print()

        if board[i] == "":
            print(" ", end = " | ")
        else:
            print(board[i], end = " | ")

    print()


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
# if firstInt == 1:
#     first = player1
# else:
#     first = player2

#first = player1 if firstInt == 1 else player2

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

    # winningPlayer = winCondition(board)
    # if winningPlayer != "":
    #     if winningPlayer == player1:
    #         print("Player 1 won.")
    #     elif winningPlayer == player2:
    #         print("Player 2 won.")
    #     else:
    #         print("It is a draw!")

    first = 1 if first == 2 else 2
        