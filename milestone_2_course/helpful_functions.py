from models.dealer import Dealer
from models.player import Player


def dealCards(player: Player, dealer: Dealer, deck: list) -> None:
    player.cards.append(deck[0])
    player.cards.append(deck[2])
    dealer.cards.append(deck[1])
    dealer.cards.append(deck[3])


def playerTurn(player: Player, dealer: Dealer, deck: list, deckIndex: int) -> int:
    moreCards = player.calculateScore() < 21

    while moreCards:
        choice = input("Do you want another card (y-n)? ")
        if choice.lower() == "y":
            player.cards.append(deck[deckIndex])
            deckIndex += 1
            moreCards = player.calculateScore() < 21
            printBoard(player, dealer, True)
        elif choice.lower() == "n":
            moreCards = False

    return deckIndex


def dealerTurn(dealer: Dealer, playerScore: int, deck: list, deckIndex: int):
    dealerScore = dealer.calculateScore()

    while dealerScore < playerScore:
        dealer.cards.append(deck[deckIndex])
        dealerScore = dealer.calculateScore()
        deckIndex += 1


def askForAnotherGame() -> bool:
    choice = input("Do you want to play another game (y-n)?")
    return choice.lower() == "y"


def printBoard(player: Player, dealer: Dealer, hidden: bool):
    print(player)
    if hidden: 
        print(dealer.hiddenPrint())
    else:
        print(dealer)