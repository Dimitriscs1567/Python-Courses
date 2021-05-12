from models.human import Human
from models.dealer import Dealer
from models.card import Card
from random import randint

def deal(human: Human, dealer: Dealer, deck: list):
    cardsIndexes = []
    while len(cardsIndexes) < 4:
        newIndex = randint(0, 51)
        if not cardsIndexes.__contains__(newIndex):
            cardsIndexes.append(newIndex)

    human.dealCards(deck[cardsIndexes[0]], deck[cardsIndexes[2]])
    dealer.dealCards(deck[cardsIndexes[1]], deck[cardsIndexes[3]])

def askForAnotherGame() -> bool:
    choice = input("Do you want to play another game? (y, n): ")
    return choice == "y"