import sys
sys.path.append("milestone_2_course/models")

from random import shuffle
from models.dealer import Dealer
from models.player import Player
from models.card import Card
from helpful_functions import askForAnotherGame, dealCards, dealerTurn, playerTurn, printBoard


deck = [
    Card("A*"), Card("A#"), Card("A-"), Card("A+"),
    Card("2*"), Card("2#"), Card("2-"), Card("2+"),
    Card("3*"), Card("3#"), Card("3-"), Card("3+"),
    Card("4*"), Card("4#"), Card("4-"), Card("4+"),
    Card("5*"), Card("5#"), Card("5-"), Card("5+"),
    Card("6*"), Card("6#"), Card("6-"), Card("6+"),
    Card("7*"), Card("7#"), Card("7-"), Card("7+"),
    Card("8*"), Card("8#"), Card("8-"), Card("8+"),
    Card("9*"), Card("9#"), Card("9-"), Card("9+"),
    Card("10*"), Card("10#"), Card("10-"), Card("10+"),
    Card("J*"), Card("J#"), Card("J-"), Card("J+"),
    Card("Q*"), Card("Q#"), Card("Q-"), Card("Q+"),
    Card("K*"), Card("K#"), Card("K-"), Card("K+"),
]

playing = True

while playing:
    player = Player()
    dealer = Dealer()

    shuffle(deck)
    dealCards(player, dealer, deck)

    printBoard(player, dealer, True)

    deckIndex = 4
    deckIndex = playerTurn(player, dealer, deck, deckIndex)
    playerScore = player.calculateScore()

    printBoard(player, dealer, False)

    if playerScore <= 21:
        dealerTurn(dealer, playerScore, deck, deckIndex)
        dealerScore = dealer.calculateScore()

        printBoard(player, dealer, False)

        if dealerScore >= playerScore and dealerScore <= 21:
            print("The dealer wins!")
        else:
            print("The player wins!")
    else:
        print("The dealer wins!")

    playing = askForAnotherGame()
