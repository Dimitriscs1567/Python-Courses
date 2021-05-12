import sys
sys.path.append("milestone_2/models")

from data import Data

def playerTurn(data: Data):
    data.print(True)
    score = data.human.calculate()
    if score >= 21:
        return score

    choice = input("Do you want to get another card? (y, n): ")
    another = choice == "y"

    while another:
        data.dealCardHuman()
        data.print(True)
        score = data.human.calculate()
        if score >= 21:
            return score

        choice = input("Do you want to get another card? (y, n): ")
        another = choice == "y"

    return score

def dealerTurn(data: Data, playerScore: int):
    score = data.dealer.calculate()

    while score < playerScore and score < 21:
        data.dealCardDealer()
        score = data.dealer.calculate()

    data.print(False)
    return score

def askForAnotherGame():
    choice = input("Do you want to play another game (y-n)? ")
    return choice.lower() == "y"

playing = True

while playing:
    gameData = Data()
    gameData.initDeal()
    
    playerScore = playerTurn(gameData)
    if playerScore < 22:
        dealerScore = dealerTurn(gameData, playerScore)
    else:
        gameData.print(False)

    if playerScore < 22 and playerScore > dealerScore:
        print("You have won!!!")
    else:
        print("The dealer won!!!")

    playing = askForAnotherGame()